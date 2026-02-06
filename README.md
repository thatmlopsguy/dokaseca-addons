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

## 👋 Introduction

Welcome to **DoKa Seca** - Distributed Orchestration Kubernetes Automation with Scalable Edge Computing Applications - a comprehensive framework for bootstrapping cloud-native platforms using Kubernetes in Docker (Kind)!

The name "DoKa Seca" is a playful Portuguese phrase where "DoKa" incorporates the "K" from Kubernetes (representing the containerized orchestration at the heart of this project), and "Seca" means "dry" - drawing inspiration from the concept of a **dry dock**. Just as ships are built, repaired, and maintained in dry docks - controlled, isolated environments where all the necessary infrastructure and tooling are readily available - DoKa Seca provides a "dry dock" for Kubernetes platforms. It creates an isolated, controlled environment where entire cloud-native platforms can be rapidly assembled, configured, and tested before being deployed to production waters.

DoKa Seca provides an opinionated, production-ready framework that automates the entire platform bootstrap process using Kind clusters. Rather than just being a collection of configurations, it's a complete platform engineering solution that provisions infrastructure, installs essential tooling, configures GitOps workflows, and sets up observability - all with a single command, in your local "dry dock" environment.

This project serves as both a personal learning journey into modern DevOps practices and a comprehensive resource for platform engineers and developers interested in rapidly spinning up production-grade Kubernetes environments. Here you'll find real-world implementations of GitOps workflows, infrastructure as code, observability stacks, and cloud-native security practices - all designed to run efficiently in local development or homelab environments while following enterprise-grade patterns and best practices.

DoKa Seca consists of 3 GitHub repositories:

| Repository                                                                       | Description                                         |
|----------------------------------------------------------------------------------|-----------------------------------------------------|
| [dokaseca-control-plane](https://github.com/thatmlopsguy/dokaseca-control-plane) | Control plane infrastructure and cluster management |
| [dokaseca-addons](https://github.com/thatmlopsguy/dokaseca-addons)               | Platform addons and Kubernetes extensions           |
| [dokaseca-workloads](https://github.com/thatmlopsguy/dokaseca-workloads)         | Application workloads and deployments               |

The Catalog is a library of curated Helm charts to create Kubernetes resources via [gitops bridge](https://github.com/gitops-bridge-dev) using argocd.

## Available Addons

This catalog contains **kubernetes addons** organized by category, all deployable via ArgoCD ApplicationSets.

### Chaos Engineering

| Tool       | Namespace  | Description                             |
|------------|------------|-----------------------------------------|
| chaos-mesh | chaos-mesh | Cloud-native chaos engineering platform |
| litmus     | litmus     | Kubernetes chaos engineering framework  |

### Cluster Management

| Tool                       | Namespace                | Description                                    |
|----------------------------|--------------------------|------------------------------------------------|
| cluster-api-operator       | capi-operator-system     | Kubernetes Cluster API Operator               |
| vcluster                   | vcluster                 | Virtual Kubernetes clusters                   |

### Compliance

| Tool                       | Namespace        | Description                                    |
|----------------------------|------------------|------------------------------------------------|
| connaisseur                | connaisseur      | Admission controller for container validation |
| kyverno                    | kyverno          | Kubernetes native policy management           |
| kyverno-policies           | kyverno          | Policy collection for Kyverno                 |
| policy-reporter            | policy-reporter  | Policy violation dashboard                     |
| polaris                    | polaris          | Kubernetes configuration validation            |

### Cost Management

| Tool                       | Namespace        | Description                                    |
|----------------------------|------------------|------------------------------------------------|
| kepler                     | kepler           | Kubernetes power consumption monitoring       |
| kube-green                 | kube-green       | Kubernetes resource scheduler for cost saving |
| opencost                   | opencost         | Real-time cost monitoring for Kubernetes      |

### Dashboard

| Tool                       | Namespace                | Description                                    |
|----------------------------|--------------------------|------------------------------------------------|
| dapr-dashboard             | dapr-system              | Dashboard for Dapr applications               |
| headlamp                   | kube-system              | Easy-to-use Kubernetes web UI                 |
| helm-dashboard             | kube-system              | Web dashboard for Helm                        |
| komoplane                  | komoplane                | Kubernetes resource browser                   |
| kubernetes-dashboard       | kubernetes-dashboard     | General-purpose web UI for Kubernetes         |

### Databases

| Tool                         | Namespace      | Description                        |
|------------------------------|----------------|------------------------------------|
| atlas-operator               | atlas-operator | Database schema migration operator |
| altinity-clickhouse-operator | kube-system    | ClickHouse database operator       |
| cloudnative-pg               | cnpg-system    | PostgreSQL operator for Kubernetes |

### Delivery

| Tool          | Namespace     | Description                                      |
|---------------|---------------|--------------------------------------------------|
| argo-cd       | argocd        | GitOps continuous delivery                       |
| argo-rollouts | argo-rollouts | Progressive delivery tool                        |
| argo-events   | argo-events   | Event-driven automation for Kubernetes           |
| devlake       | devlake       | DevOps metrics and analytics                     |
| keptn         | keptn-system  | Cloud-native application lifecycle orchestration |

### Disaster Recovery

| Tool                       | Namespace        | Description                                    |
|----------------------------|------------------|------------------------------------------------|
| velero                     | velero           | Kubernetes backup and disaster recovery        |

### GitOps

| Tool                       | Namespace        | Description                                    |
|----------------------------|------------------|------------------------------------------------|
| argocd-image-updater       | argocd           | Automatic container image update for ArgoCD   |
| gitops-promoter            | promoter-system  | Facilitates environment promotion via GitOps  |
| kargo                      | kargo            | GitOps continuous promotion                    |

### Machine Learning

| Tool     | Namespace       | Description                             |
|----------|-----------------|-----------------------------------------|
| kgateway | kgateway-system | Kubernetes API gateway for ML workloads |
| langfuse | langfuse        | LLM engineering platform                |
| litellm  | litellm         | Unified API for 100+ LLMs               |
| ollama   | ollama          | Run large language models locally       |

### Messaging

| Tool                      | Namespace       | Description                       |
|---------------------------|-----------------|-----------------------------------|
| nats                      | nats            | High-performance messaging system |
| rabbitmq-cluster-operator | rabbitmq-system | RabbitMQ cluster operator         |
| strimzi-kafka-operator    | kafka           | Apache Kafka on Kubernetes        |

### Networking

| Tool           | Namespace      | Description                                 |
|----------------|----------------|---------------------------------------------|
| cilium         | kube-system    | eBPF-based networking and security          |
| ingress-nginx  | ingress-nginx  | NGINX Ingress Controller                    |
| istio-base     | istio-system   | Istio service mesh base components          |
| istio-gateway  | istio-ingress  | Istio gateway for traffic management        |
| istiod         | istio-system   | Istio service mesh control plane            |
| kube-vip       | kube-system    | Virtual IP and load balancer for Kubernetes |
| metallb        | metallb-system | Load balancer implementation for bare metal |
| ngrok-operator | ngrok          | Secure tunnels to localhost                 |
| skupper        | skupper        | Multi-cloud communication for Kubernetes    |
| traefik        | traefik        | Modern HTTP reverse proxy and load balancer |

### Observability

| Tool                       | Namespace                     | Description                                  |
|----------------------------|-------------------------------|----------------------------------------------|
| alloy                      | monitoring                    | OpenTelemetry collector distribution         |
| fluent-bit                 | monitoring                    | Lightweight log processor and forwarder      |
| grafana-operator           | monitoring                    | Kubernetes operator for Grafana              |
| jaeger                     | monitoring                    | Distributed tracing system                   |
| kiali-operator             | kiali-operator                | Service mesh observability                   |
| kube-prometheus-stack      | monitoring                    | Complete monitoring stack with Prometheus    |
| logging-operator           | logging                       | Log management operator                      |
| loki                       | monitoring                    | Log aggregation system                       |
| opentelemetry-operator     | opentelemetry-operator-system | OpenTelemetry operator                       |
| pyroscope                  | monitoring                    | Continuous profiling platform                |
| tempo                      | monitoring                    | Distributed tracing backend                  |
| vector                     | monitoring                    | High-performance observability data pipeline |
| victoria-logs-single       | monitoring                    | Fast and cost-effective log database         |
| victoria-metrics-k8s-stack | monitoring                    | Monitoring solution and time series database |
| zipkin                     | zipkin                        | Distributed tracing system                   |

### Platform Engineering

| Tool       | Namespace         | Description                                      |
|------------|-------------------|--------------------------------------------------|
| crossplane | crossplane-system | Universal control plane for cloud resources      |
| dapr       | dapr-system       | Event-driven, portable runtime for microservices |
| karpor     | karpor            | Kubernetes resource explorer                     |
| koreo      | koreo             | Kubernetes resource orchestration                |
| kro        | kro               | Kubernetes resource optimization                 |

### Portal

| Tool                       | Namespace        | Description                                    |
|----------------------------|------------------|------------------------------------------------|
| backstage                  | backstage        | Open platform for building developer portals  |

### Security

| Tool             | Namespace        | Description                            |
|------------------|------------------|----------------------------------------|
| cert-manager     | cert-manager     | Kubernetes certificate management      |
| external-secrets | external-secrets | Kubernetes external secrets management |
| falco            | falco            | Runtime security monitoring            |
| kubearmor        | kubearmor        | Runtime security enforcement system    |
| tetragon         | kube-system      | eBPF-based security observability      |
| tracee           | tracee-system    | Linux runtime security and forensics   |
| trivy-operator   | trivy-system     | Kubernetes security scanning           |

### Storage

| Tool                       | Namespace        | Description                                    |
|----------------------------|------------------|------------------------------------------------|
| minio-operator             | minio-operator   | High performance object storage                |
| openebs                    | openebs          | Kubernetes native storage                      |

### Testing

| Tool                       | Namespace        | Description                                    |
|----------------------------|------------------|------------------------------------------------|
| report-portal              | report-portal    | Test report aggregation and visualization      |

### Utilities

| Tool       | Namespace   | Description                                        |
|------------|-------------|----------------------------------------------------|
| goldilocks | goldilocks  | Kubernetes resource recommendation                 |
| kured      | kured       | Kubernetes reboot daemon                           |
| reflector  | kube-system | Secret and ConfigMap reflection across namespaces  |
| reloader   | reloader    | Automatic restart of deployments on config changes |

### Other

| Tool                       | Namespace                        | Description                                    |
|----------------------------|----------------------------------|------------------------------------------------|
| keda                       | keda                             | Kubernetes event-driven autoscaling           |
| open-feature-operator      | open-feature-operator-system     | Feature flag management for Kubernetes        |

### Workflows

| Tool           | Namespace | Description                                      |
|----------------|-----------|--------------------------------------------------|
| airflow        | airflow   | Platform for developing and scheduling workflows |
| argo-workflows | argo      | Kubernetes-native workflow engine                |
| temporal       | temporal  | Durable execution for microservices              |

## Usage

All addons are managed through ArgoCD ApplicationSets located in the `argocd/appsets/` directory. Each addon can be
enabled by setting the appropriate cluster labels and environment variables.

For detailed instructions on how to deploy and manage these addons using ArgoCD, please refer to the [Doka Seca Addons Documentation](https://thatmlopsguy.github.io/dokaseca-control-plane/).
