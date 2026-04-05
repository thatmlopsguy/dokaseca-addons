# Copyright 2026 The Doka Seca Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# If you update this file, please follow
# https://www.thapaliya.com/en/writings/well-documented-makefiles/

# Setting SHELL to bash allows bash commands to be executed by recipes.
# Options are set to exit when a recipe line exits non-zero or a piped command fails.
SHELL = /usr/bin/env bash -o pipefail
.SHELLFLAGS = -ec

.DEFAULT_GOAL := help

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
