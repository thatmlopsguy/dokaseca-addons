# Doka Seca Addons

<div align="center">

<img src="https://raw.githubusercontent.com/thatmlopsguy/dokaseca-control-plane/main/docs/assets/logos/banner.svg" alt="DoKa Seca - Kubernetes Platform Engineering Framework" width="600"/>

</div>

<div align="center">

*Just as ships are built in dry docks, platforms are crafted in DoKa Seca*

</div>

<div align="center">
  <a href="https://github.com/thatmlopsguy/dokaseca-addons"><img src="https://img.shields.io/github/stars/thatmlopsguy/dokaseca-addons?style=flat&label=GitHub%20%E2%AD%90" alt="GitHub"></a>
  <a href="https://github.com/thatmlopsguy/dokaseca-addons/commits/main"><img src="https://img.shields.io/github/last-commit/thatmlopsguy/dokaseca-addons.svg" alt="GitHub last commit"></a>
  <a href="https://github.com/thatmlopsguy/dokaseca-addons/graphs/commit-activity"><img src="https://img.shields.io/github/commit-activity/w/thatmlopsguy/dokaseca-addons" alt="Commit activity"></a>
  <a href="https://github.com/thatmlopsguy/dokaseca-addons/issues"><img src="https://img.shields.io/github/issues/thatmlopsguy/dokaseca-addons.svg" alt="GitHub issues"></a>
  <a href="https://github.com/thatmlopsguy/dokaseca-addons/pulls"><img src="https://img.shields.io/github/issues-pr/thatmlopsguy/dokaseca-addons" alt="GitHub PRs"></a>
  <a href="https://github.com/thatmlopsguy/dokaseca-addons/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://thatmlopsguy.github.io/dokaseca-control-plane/"><img src="https://img.shields.io/website-up-down-green-red/http/shields.io.svg" alt="Website"></a>
  <a href="https://github.com/thatmlopsguy/dokaseca-addons/actions/workflows/pre-commit.yml"><img src="https://github.com/thatmlopsguy/dokaseca-addons/workflows/Pre-commit%20Checks/badge.svg" alt="Pre-commit"></a>
  <a href="https://github.com/thatmlopsguy/dokaseca-addons/actions/workflows/promoter.yml"><img src="https://github.com/thatmlopsguy/dokaseca-addons/actions/workflows/promoter.yml/badge.svg" alt="ArgoCD Promoter"></a>
</div>

>⚠️ Note
>
> DoKa Seca is still in relatively early development. At this time, **do not use** Doka Seca for critical production systems.

## Introduction

Welcome to **DoKa Seca** - Distributed Orchestration Kubernetes Automation with Scalable Edge Computing Applications - a comprehensive framework for bootstrapping cloud-native platforms using Kubernetes in Docker (Kind)!

DoKa Seca provides an opinionated, production-ready framework that automates the entire platform bootstrap process using Kind clusters. Rather than just being a collection of configurations, it's a complete platform engineering solution that provisions infrastructure, installs essential tooling, configures GitOps workflows, and sets up observability - all with a single command, in your local "dry dock" environment.

This project serves as both a personal learning journey into modern DevOps practices and a comprehensive resource for platform engineers and developers interested in rapidly spinning up production-grade Kubernetes environments. Here you'll find real-world implementations of GitOps workflows, infrastructure as code, observability stacks, and cloud-native security practices - all designed to run efficiently in local development or homelab environments while following enterprise-grade patterns and best practices.

DoKa Seca consists of 5 GitHub repositories:

| Repository                                                                         | Description                                         |
|------------------------------------------------------------------------------------|-----------------------------------------------------|
| [dokaseca-control-plane](https://github.com/thatmlopsguy/dokaseca-control-plane)   | Control plane infrastructure and cluster management |
| [dokaseca-addons](https://github.com/thatmlopsguy/dokaseca-addons)                 | Platform addons and Kubernetes extensions           |
| [dokaseca-workloads](https://github.com/thatmlopsguy/dokaseca-workloads)           | Application workloads and deployments               |
| [dokaseca-portal](https://github.com/thatmlopsguy/dokaseca-portal)                 | Backstage project (TBD) (optional)                  |
| [dokaseca-portal-catalog](https://github.com/thatmlopsguy/dokaseca-portal-catalog) | Backstage Catalog (TBD) (optional)                  |

The Catalog is a library of curated Helm charts to create Kubernetes resources via [gitops bridge](https://github.com/gitops-bridge-dev) using argocd. The list of available addons can be found in the [Catalog](docs/catalog.md).

## Usage

All addons are managed through ArgoCD ApplicationSets located in the `argocd/appsets/` directory. Each addon can be
enabled by setting the appropriate cluster labels and environment variables.

For detailed instructions on how to deploy and manage these addons using ArgoCD, please refer to the [Doka Seca Addons Documentation](https://thatmlopsguy.github.io/dokaseca-control-plane/).

## Contributing

Contributions to DoKa Seca are welcome! If you have an addon you'd like to contribute, please follow the guidelines outlined in the [Contributing Guide](CONTRIBUTING.md) and submit a pull request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
