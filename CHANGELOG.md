# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-03-30

### Added

- Add new application sets for analytics, compute, and data management tools; update strimzi version and add slurm operator values
- Add addons-paralus ApplicationSet for ArgoCD with environment-specific configurations
- Add addons-rbac-manager
- Add Jetstack chart repository to sourceRepos in project.yaml
- Add Kubernetes documentation repository to sourceRepos in project.yaml
- Add ingress configuration for headlamp in values.yaml
- Add missing ingressClassName for headlamp in values.yaml
- Add argocd-rbac-operator ApplicationSet and update promoter.yaml
- Add comment link for cron schedule in ArgoCD promoter workflow
- Add pyroscope values.yaml
- Add grafana appset
- Add missing chart reference in addons-grafana appset
- Add additional Grafana datasources for Loki, Tempo, Zipkin, and Pyroscope
- Add additional Grafana datasources for Jaeger and VictoriaMetrics logs and traces
- Add OneUptime ApplicationSet
- Add OneUptime Kubernetes Agent ApplicationSet and configuration
- Add Inspektor Gadget ApplicationSet
- Add multiple ApplicationSets for various utilities
- Add KEDA and KEDA add-ons HTTP ApplicationSets
- Add KEDA Kaito scaler ApplicationSet and related configurations

### Changed

- Update changelog
- Bump ruff from 0.15.5 to 0.15.6
- Merge pull request #53 from thatmlopsguy/dependabot/uv/ruff-0.15.6
- Update ArgoCD addon versions
- Merge pull request #52 from thatmlopsguy/promoter-23394325939
- Bump astral-sh/setup-uv from 7.3.1 to 7.6.0
- Merge pull request #54 from thatmlopsguy/dependabot/github_actions/astral-sh/setup-uv-7.6.0
- Update sourceRepos in project.yaml to include external-secrets chart repository
- Update sourceRepos in project.yaml to use wildcard and comment out specific repositories
- Update addonChartVersion for dev environment in addons-headlamp-appset.yaml
- Update ingress pathType to type in values.yaml and add new kustomization.yaml for headlamp
- Update DevLake, Velero, and Zipkin configurations
- Refactor code structure for improved readability and maintainability
- Update Grafana datasources for improved logging and tracing support
- Update version to 0.3.0 in pyproject.toml

### Fixed

- Ensure pathType is correctly set for headlamp ingress configuration in values.yaml
- Update ArgoCD promoter schedule to run monthly on the 1st
- Enable postgres backend storage and configure connection details in values.yaml
- Enable postgres backend storage and configure connection details in values.yaml
- Enable AWS S3 Mlflow Artifact Root and update configuration details in values.yaml
- Update S3 endpoint URL in extra environment variables for mlflow configuration
- Update Velero configuration for S3 backup storage and credentials
- Update project name to addons-project in ArgoCD appset
- Update project name to addons in ArgoCD appset
- Deprecate Zipkin ApplicationSet and update promoter to exclude Zipkin

### Removed

- Remove ApplicationSets for Keptn; update dependencies in promoter.yaml
- Remove mlflow values.yaml configuration file

## [0.1.1] - 2026-03-20

### Changed

- Enable persist-credentials for checkout step in release workflow

## [0.1.0] - 2026-03-20

### Added

- Add README.md
- Add appset addons
- Add catalog
- Add environment addon values
- Add kustomize addons
- Add exclude folder
- Add metalb helm values
- Add kepler appset
- Add kubernetes dashboard appset
- Add dapr dashboard appset
- Add clickhouse operator appset
- Add  helm-dashboard appset
- Add rabbitmq cluster operator appset
- Add gateway-api crd
- Add airflow appset
- Add tekton kustomization
- Add shipwright
- Add ollama appset
- Add temporal appset
- Add litellm appset
- Add Argo Workflows to the catalog
- Add addons-argo-workflows ApplicationSet
- Add addons-gateway-api ApplicationSet and kustomization files for gateway-api versions
- Add kustomization file for gateway-api v1.4.0
- Add addons-istio ApplicationSet and related values files; remove outdated istio base and gateway appsets
- Add env configuration for PILOT_ENABLE_AMBIENT in values-ztunnel.yaml
- Add PILOT_ENABLE_AMBIENT environment variable to values-istiod.yaml
- Add multiple ApplicationSets for observability addons including Alloy, OpenTelemetry, Vector, Logging, Loki, Victoria Logs, Kube Prometheus Stack, Victoria Metrics, Pyroscope, Jaeger, Tempo, and Zipkin
- Add new watchdog.yaml file with comprehensive dependencies for various OSS tools and frameworks
- Feat: add EditorConfig file for consistent coding styles and formatting
- Add dependabot configuration and update ArgoCD Watchdog workflow for automated addon version management
- Add markdown summary output for updated dependencies in ArgoCD Watchdog
- Add pip package ecosystem to dependabot configuration
- Add ruff as a development dependency and update watchdog.yaml formatting
- Add ApplicationSets for Argo Events, Fluent Bit, and Victoria Traces; Update existing appsets and enhance argocd-watchdog.py for OCI support
- Add ApplicationSets for OpenObserve and OpenSearch; update settings and watchdog.yaml for new dependencies
- Add values.yaml for OpenSearch configuration with single-node and replicas settings
- Add ApplicationSets for Grafana Operator, OpenSearch Dashboards, and Perses with environment-specific configurations
- Add values.yaml for OpenSearch Dashboards configuration
- Add ApplicationSet and Kustomization for Parca integration
- Add ApplicationSets for NVIDIA device plugin, GPU operator, Weaviate, Kuberay, LLM-D, and VLLM stack; update watchdog.yaml dependencies
- Add issue templates for bug reports and feature requests; configure pre-commit checks
- Add envoy ApplicationSet and values.yaml for Envoy integration
- Add missing sync option for ServerSideApply in addons-envoy ApplicationSet
- Add support for docker.io in fetch_oci_versions and include envoy dependency in watchdog.yaml
- Add addons-litellm-operator ApplicationSet and update promoter dependencies
- Add ApplicationSet for altinity-clickhouse-operator and update clickhouse-operator configurations in promoter
- Add new words to cSpell configuration in settings.json
- Add GitHub version fetching support and update promoter dependencies
- Add MLflow Helm chart configuration and update promoter.yaml
- Add documentation for cert-manager controller replicas and Gateway API configuration
- Add trust-manager addon configuration and values for different environments
- Add policy-controller addon configuration and values for ArgoCD
- Add gitops-promoter addon configuration and values
- Add release workflow and changelog configuration

### Changed

- Vscode settings
- Security category
- Networking and chaos engineering categories
- Appset categories
- Appset ml category
- All categories
- Bump headlamp appset version
- Kgateway appset
- Gitops promoter v0.5.0
- Bump kargo appset to 1.5
- Bump gitops promoter to v0.5.0
- Bump argocd-image-updater appset to 0.12.2
- Update README
- Update catalog
- Update gitops-promoter to version v0.8.1 and add kustomization file
- Expand available addons section in README with detailed descriptions and categories
- Merge pull request #1 from thatmlopsguy/watchdog
- Update ArgoCD addon versions
- Merge pull request #3 from thatmlopsguy/watchdog-19904819474
- Update README to include ArgoCD Watchdog badge
- Update observability dependencies in watchdog.yaml; add perses and opensearch-dashboards
- Enhance README.md with additional badges and improved introduction for DoKa Seca
- Update pre-commit workflow to ignore .vscode directory; add LICENSE file and update README links
- Update website link in README to point to the correct repository
- Update pre-commit workflow to remove Python version specification
- Update ArgoCD addon versions
- Merge pull request #4 from thatmlopsguy/watchdog-19996831948
- Merge branch 'main' of gh:thatmlopsguy/docaseca-addons
- Rename project from "argocd-watchdog" to "argocd-promoter" and implement version checking and updating functionality for ArgoCD ApplicationSets. Add new script for automated version management, update configuration files, and adjust dependencies accordingly.
- Update ArgoCD addon versions
- Merge pull request #5 from thatmlopsguy/promoter-20137235727
- Update ArgoCD addon versions
- Merge pull request #6 from thatmlopsguy/promoter-20201323266
- Bump actions/checkout from 6.0.0 to 6.0.1
- Merge pull request #7 from thatmlopsguy/dependabot/github_actions/actions/checkout-6.0.1
- Bump ruff from 0.14.7 to 0.14.8
- Merge pull request #8 from thatmlopsguy/dependabot/uv/ruff-0.14.8
- Bump ruff from 0.14.8 to 0.14.9
- Merge pull request #12 from thatmlopsguy/dependabot/uv/ruff-0.14.9
- Bump astral-sh/setup-uv from 7.1.4 to 7.1.6
- Merge pull request #11 from thatmlopsguy/dependabot/github_actions/astral-sh/setup-uv-7.1.6
- Bump actions/cache from 4.3.0 to 5.0.1
- Merge pull request #13 from thatmlopsguy/dependabot/github_actions/actions/cache-5.0.1
- Bump peter-evans/create-pull-request from 7.0.9 to 8.0.0
- Merge pull request #10 from thatmlopsguy/dependabot/github_actions/peter-evans/create-pull-request-8.0.0
- Update ArgoCD addon versions
- Merge pull request #9 from thatmlopsguy/promoter-20403377695
- Bump ruff from 0.14.9 to 0.14.10
- Merge pull request #15 from thatmlopsguy/dependabot/uv/ruff-0.14.10
- Update ArgoCD addon versions
- Merge pull request #17 from thatmlopsguy/promoter-20686379174
- Bump typer from 0.20.0 to 0.21.0
- Merge pull request #18 from thatmlopsguy/dependabot/uv/typer-0.21.0
- Update ArgoCD addon versions
- Merge pull request #19 from thatmlopsguy/promoter-20888151582
- Update pre-commit configuration and Makefile commands; add .gitkeep file
- Bump astral-sh/setup-uv from 7.1.6 to 7.2.0
- Merge pull request #22 from thatmlopsguy/dependabot/github_actions/astral-sh/setup-uv-7.2.0
- Bump ruff from 0.14.10 to 0.14.11
- Merge pull request #21 from thatmlopsguy/dependabot/uv/ruff-0.14.11
- Bump typer from 0.21.0 to 0.21.1
- Merge pull request #23 from thatmlopsguy/dependabot/uv/typer-0.21.1
- Update ArgoCD addon versions
- Merge pull request #20 from thatmlopsguy/promoter-21104618424
- Update ArgoCD addon versions
- Merge pull request #24 from thatmlopsguy/promoter-21325568255
- Bump actions/checkout from 6.0.1 to 6.0.2
- Merge pull request #25 from thatmlopsguy/dependabot/github_actions/actions/checkout-6.0.2
- Bump actions/cache from 5.0.1 to 5.0.2
- Merge pull request #26 from thatmlopsguy/dependabot/github_actions/actions/cache-5.0.2
- Bump ruff from 0.14.11 to 0.14.13
- Merge pull request #27 from thatmlopsguy/dependabot/uv/ruff-0.14.13
- Update ArgoCD addon versions
- Merge pull request #28 from thatmlopsguy/promoter-21555740342
- Bump actions/setup-python from 6.1.0 to 6.2.0
- Merge pull request #29 from thatmlopsguy/dependabot/github_actions/actions/setup-python-6.2.0
- Bump peter-evans/create-pull-request from 8.0.0 to 8.1.0
- Merge pull request #30 from thatmlopsguy/dependabot/github_actions/peter-evans/create-pull-request-8.1.0
- Bump ruff from 0.14.13 to 0.14.14
- Merge pull request #31 from thatmlopsguy/dependabot/uv/ruff-0.14.14
- Bump packaging from 25.0 to 26.0
- Merge pull request #32 from thatmlopsguy/dependabot/uv/packaging-26.0
- Bump rich from 14.2.0 to 14.3.1
- Merge pull request #33 from thatmlopsguy/dependabot/uv/rich-14.3.1
- Add report-portal application set and update promoter dependencies
- Add Dagster application set and update promoter dependencies
- Bump actions/cache from 5.0.2 to 5.0.3
- Merge pull request #36 from thatmlopsguy/dependabot/github_actions/actions/cache-5.0.3
- Bump ruff from 0.14.14 to 0.15.0
- Merge pull request #39 from thatmlopsguy/dependabot/uv/ruff-0.15.0
- Bump astral-sh/setup-uv from 7.2.0 to 7.3.0
- Merge pull request #38 from thatmlopsguy/dependabot/github_actions/astral-sh/setup-uv-7.3.0
- Update ArgoCD addon versions
- Merge pull request #37 from thatmlopsguy/promoter-22028595570
- Bump rich from 14.3.1 to 14.3.2
- Merge pull request #35 from thatmlopsguy/dependabot/uv/rich-14.3.2
- Bump typer from 0.21.1 to 0.23.1
- Merge pull request #41 from thatmlopsguy/dependabot/uv/typer-0.23.1
- Bump ruff from 0.15.0 to 0.15.1
- Merge pull request #42 from thatmlopsguy/dependabot/uv/ruff-0.15.1
- Update ArgoCD addon versions
- Merge pull request #40 from thatmlopsguy/promoter-22269167492
- Bump rich from 14.3.2 to 14.3.3
- Merge pull request #45 from thatmlopsguy/dependabot/uv/rich-14.3.3
- Update ArgoCD addon versions
- Merge pull request #43 from thatmlopsguy/promoter-22534858632
- Bump typer from 0.23.1 to 0.24.1
- Merge pull request #44 from thatmlopsguy/dependabot/uv/typer-0.24.1
- Bump ruff from 0.15.1 to 0.15.2
- Merge pull request #46 from thatmlopsguy/dependabot/uv/ruff-0.15.2
- Update pre-commit hook versions in .pre-commit-config.yaml
- Update gitops-promoter to version 0.22.7 and remove obsolete versions
- Update version to 0.2.0 in pyproject.toml
- Bump astral-sh/setup-uv from 7.3.0 to 7.3.1
- Merge pull request #48 from thatmlopsguy/dependabot/github_actions/astral-sh/setup-uv-7.3.1
- Bump ruff from 0.15.2 to 0.15.4
- Merge pull request #49 from thatmlopsguy/dependabot/uv/ruff-0.15.4
- Bump ruff from 0.15.4 to 0.15.5
- Merge pull request #51 from thatmlopsguy/dependabot/uv/ruff-0.15.5
- Update ArgoCD addon versions
- Merge pull request #50 from thatmlopsguy/promoter-23102394485
- Correct typo in LDAP Lookup Bind comment across environment values
- Update gitops-promoter addon configuration and dependencies

### Fixed

- Control-plane addons values
- Metallb appset
- Gitops promoter appset
- Gitops promoter appset
- Argocd project location
- Kepler appset
- Gitops promoter appset
- Headlamp addonChartRepository
- Headlamp kustomize
- Headlamp kustomize
- Headlamp kustomize
- Headlamp kustomize
- K8s dashboard appset
- Disable kong proxy
- Change project from addons to default in addons-ingress-nginx ApplicationSet
- Change project from default to addons in addons-ingress-nginx ApplicationSet
- Update addonKustomizeVersion to v0.18.2 in addons-gitops-promoter ApplicationSet
- Update ApplicationSet name format to include addonChart in addons-istio appset
- Update releaseName format in addons-istio ApplicationSet to use addonChart
- Update kube-green repository URL to point to the official source
- Comment out unused GitHub Security Lab action in ArgoCD Watchdog workflow
- Update branch name for automated ArgoCD addon version updates
- Update token reference in ArgoCD Watchdog workflow
- Improve output formatting for update summary in ArgoCD Watchdog
- Enhance summary output delimiter in ArgoCD Watchdog
- Streamline summary output handling in ArgoCD Watchdog
- Update pyproject.toml and argocd-watchdog.py for improved linting and code clarity
- Correct addonChart and addonChartName references in addons-envoy ApplicationSet
- Update ignore rule in zizmor.yml to reference promoter.yml instead of watchdog.yml

### Removed

- Delete aso2 addon in gcp
- Remove outdated kustomization file for gateway-api v1.4.0
- Remove allInOne configuration and set profile to ambient in values-cni.yaml
- Remove outdated update summary file and add to .gitignore
- Remove unused variable 'field_name' in update function

[0.3.0]: https://github.com/thatmlopsguy/dokaseca-addons/compare/v0.1.1..v0.3.0
[0.1.1]: https://github.com/thatmlopsguy/dokaseca-addons/compare/v0.1.0..v0.1.1
[0.1.0]: https://github.com/thatmlopsguy/dokaseca-addons/tree/v0.1.0

<!-- generated by git-cliff -->
