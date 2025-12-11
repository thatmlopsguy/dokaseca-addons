#!/usr/bin/env python3
"""
ArgoCD Watchdog - Automated Version Checker for ApplicationSets

This script monitors ArgoCD ApplicationSet files for version updates
based on comments marked with '# watchdog this'.
"""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import typer
import yaml
from packaging import version
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="ArgoCD ApplicationSet version watchdog")
console = Console()


def load_config(config_path: Path) -> dict:
    """Load the watchdog configuration file."""
    try:
        with open(config_path) as f:
            return yaml.safe_load(f)
    except Exception as e:
        console.print(f"[red]Error loading config file: {e}[/red]")
        raise typer.Exit(1)  # noqa: B904


def fetch_rss_versions(rss_url: str) -> list[str]:
    """Fetch available versions from an RSS feed."""
    try:
        response = requests.get(rss_url, timeout=10)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        versions = []

        # Parse RSS feed for version numbers
        for item in root.findall(".//item"):
            title = item.find("title")
            if title is not None and title.text:
                # Extract version from title (assuming format like "chaos-mesh 2.7.0")
                match = re.search(r"(\d+\.\d+\.\d+)", title.text)
                if match:
                    versions.append(match.group(1))

        return versions
    except Exception as e:
        console.print(f"[yellow]Warning: Could not fetch RSS feed: {e}[/yellow]")
        return []


def fetch_oci_versions(oci_url: str) -> list[str]:
    """
    Fetch available versions from an OCI registry.

    Supports OCI URLs in the format: oci://registry/repository/image
    Currently supports ghcr.io and docker.io with anonymous access.
    Handles pagination to retrieve all tags.
    """
    try:
        # Parse OCI URL: oci://ghcr.io/ariga/charts/atlas-operator
        if oci_url.startswith("oci://"):
            oci_url = oci_url[6:]  # Remove 'oci://' prefix

        parts = oci_url.split("/", 1)
        if len(parts) != 2:
            console.print(f"[yellow]Warning: Invalid OCI URL format: {oci_url}[/yellow]")
            return []

        registry = parts[0]
        repository = parts[1]

        # Get anonymous token for the registry
        token = _get_oci_token(registry, repository)

        # Determine the actual API endpoint (Docker Hub uses registry-1.docker.io)
        api_registry = registry
        if registry == "docker.io":
            api_registry = "registry-1.docker.io"

        # Fetch all tags from the registry (with pagination)
        all_tags = []
        tags_url: str | None = f"https://{api_registry}/v2/{repository}/tags/list"
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"

        while tags_url:
            response = requests.get(tags_url, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()
            tags = data.get("tags", [])
            all_tags.extend(tags)

            # Check for pagination via Link header
            tags_url = _get_next_page_url(response, api_registry)

        # Filter to only include valid semver-like versions
        # Supports both with and without 'v' prefix (e.g., 1.2.3, v1.2.3)
        # Excludes pre-release versions like -alpha, -beta, -rc, -main unless they're the only option
        versions = []
        for tag in all_tags:
            # Match semantic versions with optional 'v' prefix (e.g., 1.2.3, v1.2.3)
            # Exclude pre-release suffixes like -alpha, -beta, -rc, -main
            if re.match(r"^v?\d+\.\d+\.\d+$", tag):
                # Strip 'v' prefix for consistent version comparison
                versions.append(tag.lstrip("v"))

        return versions
    except Exception as e:
        console.print(f"[yellow]Warning: Could not fetch OCI tags: {e}[/yellow]")
        return []


def _get_next_page_url(response: requests.Response, registry: str) -> str | None:
    """
    Extract the next page URL from the Link header for OCI registry pagination.

    The Link header format is: <url>; rel="next"
    """
    link_header = response.headers.get("Link", "")
    if not link_header:
        return None

    # Parse Link header: </v2/repo/tags/list?last=tag&n=100>; rel="next"
    match = re.search(r'<([^>]+)>;\s*rel="next"', link_header)
    if match:
        next_path = match.group(1)
        # Handle relative URLs
        if next_path.startswith("/"):
            return f"https://{registry}{next_path}"
        return next_path
    return None


def _get_oci_token(registry: str, repository: str) -> str | None:
    """
    Get an authentication token for an OCI registry.

    Supports anonymous token retrieval for public repositories.
    """
    try:
        if registry == "ghcr.io":
            # GitHub Container Registry token endpoint
            token_url = f"https://ghcr.io/token?scope=repository:{repository}:pull"
            response = requests.get(token_url, timeout=10)
            response.raise_for_status()
            return response.json().get("token")
        elif registry in ("registry.hub.docker.com", "docker.io"):
            # Docker Hub token endpoint
            token_url = f"https://auth.docker.io/token?service=registry.docker.io&scope=repository:{repository}:pull"
            response = requests.get(token_url, timeout=10)
            response.raise_for_status()
            return response.json().get("token")
        else:
            # Try without authentication for other registries
            return None
    except Exception as e:
        console.print(f"[yellow]Warning: Could not get OCI token: {e}[/yellow]")
        return None


def find_watchdog_lines(file_path: Path) -> list[tuple[int, str, str]]:
    """
    Find lines in YAML file marked with '# watchdog this'.

    Returns:
        List of tuples: (line_number, field_name, current_version)
    """
    try:
        with open(file_path) as f:
            lines = f.readlines()

        watchdog_lines = []
        for i, line in enumerate(lines, start=1):
            if "# watchdog this" in line:
                # Extract field name and version
                # Pattern: addonChartVersion: 2.7.0 # watchdog this
                match = re.match(r"\s*(\w+):\s*([^\s#]+)", line)
                if match:
                    field_name = match.group(1)
                    current_version = match.group(2)
                    watchdog_lines.append((i, field_name, current_version))

        return watchdog_lines
    except Exception as e:
        console.print(f"[yellow]Warning: Could not read file {file_path}: {e}[/yellow]")
        return []


def get_latest_version(versions: list[str]) -> str | None:
    """Get the latest version from a list of version strings."""
    if not versions:
        return None

    try:
        parsed_versions = [version.parse(v) for v in versions]
        latest = max(parsed_versions)
        return str(latest)
    except Exception:
        return versions[0] if versions else None


@app.command()
def check(
    config_file: Path = typer.Option(  # noqa: B008
        "watchdog.yaml",
        "--config",
        "-c",
        help="Path to the watchdog configuration file",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        "-n",
        help="Show what would be checked without making any changes",
    ),
):
    """
    Check for new versions based on watchdog configuration.

    Reads the configuration file, finds files with '# watchdog this' comments,
    and checks for available updates from the specified repositories.
    """
    if dry_run:
        console.print("[blue]DRY RUN MODE - No changes will be made[/blue]\n")
    if not config_file.exists():
        console.print(f"[red]Error: Config file not found: {config_file}[/red]")
        raise typer.Exit(1)

    console.print(f"[blue]Loading configuration from {config_file}...[/blue]")
    config = load_config(config_file)

    if "dependencies" not in config:
        console.print("[red]Error: No 'dependencies' section in config file[/red]")
        raise typer.Exit(1)

    table = Table(title="Version Check Results")
    table.add_column("Dependency", style="cyan")
    table.add_column("File", style="magenta")
    table.add_column("Current Version", style="yellow")
    table.add_column("Latest Version", style="green")
    table.add_column("Status", style="bold")

    updates_available = 0

    for dep in config["dependencies"]:
        dep_name = dep.get("name", "Unknown")
        source_file = dep.get("source", {}).get("file")
        repo_info = dep.get("repository", {})

        if not source_file:
            console.print(f"[yellow]Warning: No source file for {dep_name}[/yellow]")
            continue

        file_path = Path(source_file)
        if not file_path.exists():
            console.print(f"[yellow]Warning: File not found: {file_path}[/yellow]")
            continue

        if verbose:
            console.print(f"\n[blue]Checking {dep_name}...[/blue]")

        # Find lines marked with watchdog
        watchdog_lines = find_watchdog_lines(file_path)

        if not watchdog_lines:
            if verbose:
                console.print(f"[yellow]No watchdog markers found in {file_path}[/yellow]")
            continue

        # Fetch available versions
        available_versions = []
        repo_type = repo_info.get("type")
        repo_url = repo_info.get("url")
        if repo_type == "rss" and repo_url:
            available_versions = fetch_rss_versions(repo_url)
        elif repo_type == "oci" and repo_url:
            available_versions = fetch_oci_versions(repo_url)

        latest_version = get_latest_version(available_versions)

        for _line_num, _field_name, current_ver in watchdog_lines:
            status = "✓ Up to date"
            status_style = "green"

            if latest_version:
                try:
                    if version.parse(latest_version) > version.parse(current_ver):
                        status = "⚠ Update available"
                        status_style = "bold yellow"
                        updates_available += 1
                except Exception:
                    status = "? Unknown"
                    status_style = "dim"
            else:
                status = "? Cannot check"
                status_style = "dim"

            table.add_row(
                dep_name,
                str(file_path.name),
                current_ver,
                latest_version or "N/A",
                f"[{status_style}]{status}[/{status_style}]",
            )

    console.print("\n")
    console.print(table)
    console.print("\n")

    if updates_available > 0:
        console.print(f"[yellow]Found {updates_available} update(s) available![/yellow]")
        sys.exit(1)
    else:
        console.print("[green]All dependencies are up to date![/green]")
        sys.exit(0)


def update_version_in_file(
    file_path: Path,
    line_num: int,
    old_version: str,
    new_version: str,
    dry_run: bool = False,
) -> bool:
    """
    Update a version in a YAML file.

    Args:
        file_path: Path to the file to update
        line_num: Line number to update (1-indexed)
        old_version: Current version to replace
        new_version: New version to set
        dry_run: If True, don't actually modify the file

    Returns:
        True if update was successful (or would be in dry-run mode)
    """
    try:
        with open(file_path) as f:
            lines = f.readlines()

        if line_num > len(lines):
            return False

        original_line = lines[line_num - 1]
        updated_line = original_line.replace(old_version, new_version)

        if original_line == updated_line:
            return False

        if not dry_run:
            lines[line_num - 1] = updated_line
            with open(file_path, "w") as f:
                f.writelines(lines)

        return True
    except Exception as e:
        console.print(f"[red]Error updating file: {e}[/red]")
        return False


@app.command()
def update(
    config_file: Path = typer.Option(  # noqa: B008
        "watchdog.yaml",
        "--config",
        "-c",
        help="Path to the watchdog configuration file",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        "-n",
        help="Show what would be updated without making any changes",
    ),
    apply: bool = typer.Option(
        False,
        "--apply",
        "-a",
        help="Apply the updates (required to actually modify files)",
    ),
):
    """
    Update versions in files based on watchdog configuration.

    Automatically updates version strings in files marked with '# watchdog this'
    to their latest available versions.

    Requires --apply flag to actually modify files.
    """
    # Validate flags
    if dry_run and apply:
        console.print("[red]Error: Cannot use both --dry-run and --apply together[/red]")
        raise typer.Exit(1)

    if not dry_run and not apply:
        console.print("[yellow]No action specified. Use --dry-run to preview or --apply to update files.[/yellow]")
        raise typer.Exit(1)

    if dry_run:
        console.print("[blue]DRY RUN MODE - No files will be modified[/blue]\n")
    elif apply:
        console.print("[yellow]APPLY MODE - Files will be modified[/yellow]\n")

    if not config_file.exists():
        console.print(f"[red]Error: Config file not found: {config_file}[/red]")
        raise typer.Exit(1)

    console.print(f"[blue]Loading configuration from {config_file}...[/blue]")
    config = load_config(config_file)

    if "dependencies" not in config:
        console.print("[red]Error: No 'dependencies' section in config file[/red]")
        raise typer.Exit(1)

    table = Table(title="Update Results")
    table.add_column("Dependency", style="cyan")
    table.add_column("File", style="magenta")
    table.add_column("Old Version", style="yellow")
    table.add_column("New Version", style="green")
    table.add_column("Status", style="bold")

    updates_made = 0
    updates_skipped = 0
    markdown_rows = []

    for dep in config["dependencies"]:
        dep_name = dep.get("name", "Unknown")
        source_file = dep.get("source", {}).get("file")
        repo_info = dep.get("repository", {})

        if not source_file:
            console.print(f"[yellow]Warning: No source file for {dep_name}[/yellow]")
            continue

        file_path = Path(source_file)
        if not file_path.exists():
            console.print(f"[yellow]Warning: File not found: {file_path}[/yellow]")
            continue

        if verbose:
            console.print(f"\n[blue]Processing {dep_name}...[/blue]")

        # Find lines marked with watchdog
        watchdog_lines = find_watchdog_lines(file_path)

        if not watchdog_lines:
            if verbose:
                console.print(f"[yellow]No watchdog markers found in {file_path}[/yellow]")
            continue

        # Fetch available versions
        available_versions = []
        repo_type = repo_info.get("type")
        repo_url = repo_info.get("url")
        if repo_type == "rss" and repo_url:
            available_versions = fetch_rss_versions(repo_url)
        elif repo_type == "oci" and repo_url:
            available_versions = fetch_oci_versions(repo_url)

        latest_version = get_latest_version(available_versions)

        for line_num, _field_name, current_ver in watchdog_lines:
            status = "⊘ Skipped"
            status_style = "dim"

            if latest_version:
                try:
                    if version.parse(latest_version) > version.parse(current_ver):
                        # Update needed
                        success = update_version_in_file(
                            file_path,
                            line_num,
                            current_ver,
                            latest_version,
                            dry_run=not apply,
                        )

                        if success:
                            if not apply:
                                status = "→ Would update"
                                status_style = "blue"
                            else:
                                status = "✓ Updated"
                                status_style = "green"
                            updates_made += 1
                        else:
                            status = "✗ Failed"
                            status_style = "red"
                    else:
                        status = "✓ Already latest"
                        status_style = "green"
                        updates_skipped += 1
                except Exception as e:
                    status = f"✗ Error: {str(e)}"
                    status_style = "red"
                    updates_skipped += 1
            else:
                status = "? Cannot check"
                status_style = "yellow"
                updates_skipped += 1

            table.add_row(
                dep_name,
                str(file_path.name),
                current_ver,
                latest_version or "N/A",
                f"[{status_style}]{status}[/{status_style}]",
            )

            # Add to markdown table if updated or would be updated
            if "Updated" in status or "Would update" in status:
                markdown_rows.append(
                    f"| {dep_name} | {file_path.name} | {current_ver} | {latest_version or 'N/A'} | {status.replace('→', '').replace('✓', '').strip()} |"
                )

    console.print("\n")
    console.print(table)
    console.print("\n")

    # Output markdown table for GitHub Actions
    if markdown_rows:
        markdown_table = "| Dependency | File | Old Version | New Version | Status |\n"
        markdown_table += "|------------|------|-------------|-------------|--------|\n"
        markdown_table += "\n".join(markdown_rows)

        # Write to file for GitHub Actions to read
        with open("update-summary.md", "w") as f:
            f.write(markdown_table)

        if verbose:
            console.print("[blue]Markdown summary written to update-summary.md[/blue]\n")

    if updates_made > 0:
        if not apply:
            console.print(f"[blue]Would update {updates_made} version(s) (dry-run mode)[/blue]")
            console.print("[dim]Run with --apply to actually modify files[/dim]")
        else:
            console.print(f"[green]Successfully updated {updates_made} version(s)![/green]")
    else:
        console.print("[green]No updates needed - all versions are current![/green]")

    if updates_skipped > 0 and verbose:
        console.print(f"[dim]Skipped {updates_skipped} item(s)[/dim]")


@app.command()
def validate(
    config_file: Path | None = None,
):
    """
    Validate the watchdog configuration file.

    Checks that the configuration file is valid and all referenced files exist.
    """
    if config_file is None:
        config_file = typer.Option(
            "watchdog.yaml",
            "--config",
            "-c",
            help="Path to the watchdog configuration file",
        )

    if not config_file.exists():
        console.print(f"[red]Error: Config file not found: {config_file}[/red]")
        raise typer.Exit(1)

    console.print(f"[blue]Validating configuration from {config_file}...[/blue]\n")

    try:
        config = load_config(config_file)
    except Exception:
        raise typer.Exit(1)  # noqa: B904

    if "dependencies" not in config:
        console.print("[red]✗ No 'dependencies' section in config file[/red]")
        raise typer.Exit(1)

    console.print("[green]✓ Config file is valid YAML[/green]")
    console.print(f"[green]✓ Found {len(config['dependencies'])} dependencies[/green]\n")

    errors = 0
    for i, dep in enumerate(config["dependencies"], 1):
        dep_name = dep.get("name", f"Dependency #{i}")
        console.print(f"[cyan]Checking {dep_name}...[/cyan]")

        source_file = dep.get("source", {}).get("file")
        if not source_file:
            console.print("  [red]✗ No source file specified[/red]")
            errors += 1
            continue

        file_path = Path(source_file)
        if not file_path.exists():
            console.print(f"  [red]✗ File not found: {file_path}[/red]")
            errors += 1
            continue

        console.print(f"  [green]✓ Source file exists: {file_path}[/green]")

        # Check for watchdog markers
        watchdog_lines = find_watchdog_lines(file_path)
        if watchdog_lines:
            console.print(f"  [green]✓ Found {len(watchdog_lines)} watchdog marker(s)[/green]")
            for line_num, field_name, current_ver in watchdog_lines:
                console.print(f"    Line {line_num}: {field_name} = {current_ver}")
        else:
            console.print("  [yellow]⚠ No watchdog markers found[/yellow]")

        # Check repository configuration
        repo_info = dep.get("repository", {})
        repo_type = repo_info.get("type")
        if repo_type == "rss":
            if repo_info.get("url"):
                console.print("  [green]✓ RSS feed configured[/green]")
            else:
                console.print("  [red]✗ RSS feed URL missing[/red]")
                errors += 1
        elif repo_type == "oci":
            if repo_info.get("url"):
                console.print("  [green]✓ OCI registry configured[/green]")
            else:
                console.print("  [red]✗ OCI registry URL missing[/red]")
                errors += 1

        console.print()

    if errors > 0:
        console.print(f"[red]Validation failed with {errors} error(s)[/red]")
        raise typer.Exit(1)
    else:
        console.print("[green]✓ Validation successful![/green]")


if __name__ == "__main__":
    app()
