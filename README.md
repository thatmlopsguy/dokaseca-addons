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

The Catalog is a library of curated Helm charts to create Kubernetes resources via [gitops bridge](https://github.com/gitops-bridge-dev) using argocd.

## Available Addons

This catalog contains **kubernetes addons** organized by category, all deployable via ArgoCD ApplicationSets.

### Addons List

| Category              | Tool                         | Namespace                     | Description                                                                     |
|-----------------------|------------------------------|-------------------------------|---------------------------------------------------------------------------------|
| Artifact Repositories | harbor                       | harbor                        | Cloud-native registry for artifacts                                             |
| Artifact Repositories | chartmuseum                  | chartmuseum                   | Helm chart repository server                                                    |
| Analytics             | flink                        | flink-system                  | Stream processing framework                                                     |
| Analytics             | trino                        | trino                         | Distributed SQL query engine                                                    |
| Analytics             | superset                     | superset                      | Data exploration and visualization platform                                     |
| Chaos Engineering     | chaos-mesh                   | chaos-mesh                    | Cloud-native chaos engineering platform                                         |
| Chaos Engineering     | litmus                       | litmus                        | Kubernetes chaos engineering framework                                          |
| Cluster Management    | cluster-api-operator         | capi-operator-system          | Kubernetes Cluster API Operator                                                 |
| Cluster Management    | vcluster                     | vcluster                      | Virtual Kubernetes clusters                                                     |
| Compliance            | connaisseur                  | connaisseur                   | Admission controller for container validation                                   |
| Compliance            | kyverno                      | kyverno                       | Kubernetes native policy management                                             |
| Compliance            | kyverno-policies             | kyverno                       | Policy collection for Kyverno                                                   |
| Compliance            | policy-reporter              | policy-reporter               | Policy violation dashboard                                                      |
| Compliance            | polaris                      | polaris                       | Kubernetes configuration validation                                             |
| Compliance            | policy-controller            | cosign-system                 | Kubernetes admission controller for Sigstore                                    |
| Compute               | spark-operator               | spark                         | Kubernetes operator for Apache Spark                                            |
| Compute               | kuberay                      | kuberay                       | Kubernetes operator for Ray                                                     |
| Compute               | slurm-operator               | slinky                        | Kubernetes operator for Slurm                                                   |
| Cost Management       | kepler                       | kepler                        | Kubernetes power consumption monitoring                                         |
| Cost Management       | kube-green                   | kube-green                    | Kubernetes resource scheduler for cost saving                                   |
| Cost Management       | opencost                     | opencost                      | Real-time cost monitoring for Kubernetes                                        |
| Cost Management       | goldilocks                   | goldilocks                    | Kubernetes resource recommendation                                              |
| Dashboard             | dapr-dashboard               | dapr-system                   | Dashboard for Dapr applications                                                 |
| Dashboard             | headlamp                     | kube-system                   | Easy-to-use Kubernetes web UI                                                   |
| Dashboard             | helm-dashboard               | kube-system                   | Web dashboard for Helm                                                          |
| Dashboard             | komoplane                    | komoplane                     | Kubernetes resource browser                                                     |
| Data Management       | datahub                      | datahub                       | Metadata platform for data discovery                                            |
| Data Management       | feast                        | feast                         | Feature store for machine learning                                              |
| Databases             | atlas-operator               | atlas-operator                | Database schema migration operator                                              |
| Databases             | altinity-clickhouse-operator | kube-system                   | ClickHouse database operator                                                    |
| Databases             | clickhouse-operator          | clickhouse-operator-system    | ClickHouse database operator                                                    |
| Databases             | cloudnative-pg               | cnpg-system                   | PostgreSQL operator for Kubernetes                                              |
| Delivery              | argo-cd                      | argocd                        | GitOps continuous delivery                                                      |
| Delivery              | argo-rollouts                | argo-rollouts                 | Progressive delivery tool                                                       |
| Delivery              | argo-events                  | argo-events                   | Event-driven automation for Kubernetes                                          |
| Delivery              | devlake                      | devlake                       | DevOps metrics and analytics                                                    |
| Disaster Recovery     | velero                       | velero                        | Kubernetes backup and disaster recovery                                         |
| GitOps                | argocd-image-updater         | argocd                        | Automatic container image update for ArgoCD                                     |
| GitOps                | gitops-promoter              | promoter-system               | Facilitates environment promotion via GitOps                                    |
| GitOps                | kargo                        | kargo                         | GitOps continuous promotion                                                     |
| Machine Learning      | kuberay                      | kuberay                       | Kubernetes operator for Ray                                                     |
| Machine Learning      | vllm                         | vllm                          | High-performance LLM serving platform                                           |
| Machine Learning      | llm-d                        | llm-d                         | LLM deployment and management platform                                          |
| Machine Learning      | langfuse                     | langfuse                      | LLM engineering platform                                                        |
| Machine Learning      | litellm                      | litellm                       | Unified API for 100+ LLMs                                                       |
| Machine Learning      | litellm-operator             | litellm-operator              | Kubernetes operator for LiteLLM                                                 |
| Machine Learning      | ollama                       | ollama                        | Run large language models locally                                               |
| Machine Learning      | mlflow                       | mlflow                        | Open source platform for the machine learning lifecycle                         |
| Messaging             | nats                         | nats                          | High-performance messaging system                                               |
| Messaging             | rabbitmq-cluster-operator    | rabbitmq-system               | RabbitMQ cluster operator                                                       |
| Messaging             | strimzi-kafka-operator       | strimzi-system                | Apache Kafka on Kubernetes                                                      |
| Networking            | cilium                       | kube-system                   | eBPF-based networking and security                                              |
| Networking            | ingress-nginx                | ingress-nginx                 | NGINX Ingress Controller                                                        |
| Networking            | istio                        | istio-system                  | Istio service mesh                                                              |
| Networking            | kube-vip                     | kube-system                   | Virtual IP and load balancer for Kubernetes                                     |
| Networking            | metallb                      | metallb-system                | Load balancer implementation for bare metal                                     |
| Networking            | ngrok-operator               | ngrok                         | Secure tunnels to localhost                                                     |
| Networking            | skupper                      | skupper                       | Multi-cloud communication for Kubernetes                                        |
| Networking            | traefik                      | traefik                       | Modern HTTP reverse proxy and load balancer                                     |
| Networking            | kgateway                     | kgateway-system               | Kubernetes API gateway                                                          |
| Observability         | signoz                       | platform                      | Open source APM and observability platform                                      |
| Observability         | uptrace                      | monitoring                    | Distributed tracing and error monitoring                                        |
| Observability         | alertmanager                 | monitoring                    | Prometheus Alertmanager                                                         |
| Observability         | node-exporter                | monitoring                    | Prometheus Node Exporter                                                        |
| Observability         | kube-state-metrics           | monitoring                    | Kubernetes cluster state metrics exporter                                       |
| Observability         | alloy                        | monitoring                    | OpenTelemetry collector distribution                                            |
| Observability         | fluent-bit                   | monitoring                    | Lightweight log processor and forwarder                                         |
| Observability         | grafana-operator             | monitoring                    | Kubernetes operator for Grafana                                                 |
| Observability         | jaeger                       | monitoring                    | Distributed tracing system                                                      |
| Observability         | kiali-operator               | kiali-operator                | Service mesh observability                                                      |
| Observability         | kube-prometheus-stack        | monitoring                    | Complete monitoring stack with Prometheus                                       |
| Observability         | logging-operator             | logging                       | Log management operator                                                         |
| Observability         | loki                         | monitoring                    | Log aggregation system                                                          |
| Observability         | opentelemetry-operator       | opentelemetry-operator-system | OpenTelemetry operator                                                          |
| Observability         | pyroscope                    | monitoring                    | Continuous profiling platform                                                   |
| Observability         | tempo                        | monitoring                    | Distributed tracing backend                                                     |
| Observability         | vector                       | monitoring                    | High-performance observability data pipeline                                    |
| Observability         | victoria-logs-single         | monitoring                    | Fast and cost-effective log database                                            |
| Observability         | victoria-metrics-k8s-stack   | monitoring                    | Monitoring solution and time series database                                    |
| Platform Engineering  | crossplane                   | crossplane-system             | Universal control plane for cloud resources                                     |
| Platform Engineering  | dapr                         | dapr-system                   | Event-driven, portable runtime for microservices                                |
| Platform Engineering  | karpor                       | karpor                        | Kubernetes resource explorer                                                    |
| Platform Engineering  | koreo                        | koreo                         | Kubernetes resource orchestration                                               |
| Platform Engineering  | kro                          | kro                           | Kubernetes resource optimization                                                |
| Portal                | backstage                    | backstage                     | Open platform for building developer portals                                    |
| RBAC                  | rbac-manager                 | rbac-manager                  | Kubernetes RBAC management                                                      |
| RBAC                  | argocd-rbac-operator         | argocd-rbac-operator-system   | Kubernetes RBAC management for ArgoCD                                           |
| RBAC                  | paralus                      | paralus                       | Kubernetes RBAC management and visualization                                    |
| Scheduling            | volcano                      | volcano-system                | High-performance batch scheduling system                                        |
| Scheduling            | yunikorn                     | yunikorn-system               | Kubernetes scheduler for big data workloads                                     |
| Scheduling            | kueue                        | kueue-system                  | Kubernetes-native job scheduling system                                         |
| Security              | cert-manager                 | cert-manager                  | Kubernetes certificate management                                               |
| Security              | external-secrets             | external-secrets              | Kubernetes external secrets management                                          |
| Security              | falco                        | falco                         | Runtime security monitoring                                                     |
| Security              | kubearmor                    | kubearmor                     | Runtime security enforcement system                                             |
| Security              | tetragon                     | kube-system                   | eBPF-based security observability                                               |
| Security              | tracee                       | tracee-system                 | Linux runtime security and forensics                                            |
| Security              | trivy-operator               | trivy-system                  | Kubernetes security scanning                                                    |
| Security              | trust-manager                | trust-manager                 | Manage TLS trust bundles in Kubernetes                                          |
| Security              | dependency-track             | dependency-track              | Software supply chain security                                                  |
| Storage               | minio-operator               | minio-operator                | High performance object storage                                                 |
| Storage               | openebs                      | openebs                       | Kubernetes native storage                                                       |
| Storage               | longhorn                     | longhorn-system               | Cloud-native distributed block storage for Kubernetes                           |
| Storage               | rook-ceph                    | rook-ceph                     | Cloud-native distributed storage orchestrator for Kubernetes                    |
| Testing               | report-portal                | report-portal                 | Test report aggregation and visualization                                       |
| Utilities             | kured                        | kured                         | Kubernetes reboot daemon                                                        |
| Utilities             | reflector                    | kube-system                   | Secret and ConfigMap reflection across namespaces                               |
| Utilities             | reloader                     | reloader                      | Automatic restart of deployments on config changes                              |
| Utilities             | inspektor-gadget             | inspektor-gadget              | Kubernetes runtime security and observability                                   |
| Utilities             | eraser                       | eraser                        | Kubernetes resource cleanup utility                                             |
| Utilities             | fake-gpu-operator            | gpu-operator                  | Simulate GPU resources in Kubernetes                                            |
| Utilities             | spegel                       | spegel                        | Stateless cluster local OCI registry mirror                                     |
| Utilities             | kube-image-keeper            | kuik-system                   | Container image caching system for Kubernetes                                   |
| Utilities             | kubernetes-replicator        | kube-system                   | Kubernetes controller for synchronizing secrets & config maps across namespaces |
| Other                 | open-feature-operator        | open-feature-operator-system  | Feature flag management for Kubernetes                                          |
| Scaling               | keda                         | keda                          | Kubernetes-based Event Driven Autoscaling                                       |
| Scaling               | keda-add-ons-http            | keda                          | keda add-on for HTTP-based scaling                                              |
| Scaling               | keda-kaito-scaler            | keda                          | keda add-on for LLM inference scaling                                           |
| Workflows             | airflow                      | airflow                       | Platform for developing and scheduling workflows                                |
| Workflows             | argo-workflows               | argo                          | Kubernetes-native workflow engine                                               |
| Workflows             | temporal                     | temporal                      | Durable execution for microservices                                             |
| Workflows             | dagster                      | dagster                       | Data orchestrator for machine learning, analytics, and ETL                      |

## Usage

All addons are managed through ArgoCD ApplicationSets located in the `argocd/appsets/` directory. Each addon can be
enabled by setting the appropriate cluster labels and environment variables.

For detailed instructions on how to deploy and manage these addons using ArgoCD, please refer to the [Doka Seca Addons Documentation](https://thatmlopsguy.github.io/dokaseca-control-plane/).
