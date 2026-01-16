all: help

.PHONY: help
##@ General
help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage: \033[36m\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-26s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Development
.PHONY: pre-commit-install pre-commit-run pre-commit-update
pre-commit-run: ## Execute pre-commit git-hooks
	@uvx prek run -a

pre-commit-install: ## Install pre-commit git-hooks
	@uvx prek install

pre-commit-update: ## Update pre-commit git-hooks
	@uvx pre-commit-update

argocd-promoter-update: ## Update ArgoCD ApplicationSet definitions from promoter.yaml
	@uv run src/argocd-promoter.py update --dry-run
