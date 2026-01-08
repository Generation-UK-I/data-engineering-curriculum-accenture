SHELL=bash
default: help

# this include is only going to include the tools.mk after the submodules have been pulled down
include $(wildcard academy-presentation-tooling/makefiles/tools.mk)

# Valid values are "schooloftech", "ngeindia"
a=schooloftech
current_folder=$(shell pwd)

.PHONY: help
help:
	@awk -F ':|##' '/^[^\t].+?:.*?##/ {printf "\033[36m%-30s\033[0m  %s\n", $$1, $$NF}' $(MAKEFILE_LIST) $(wildcard makefiles/*.mk) | sort | uniq

npm-install:
	@ echo 'Installing NPM dependencies'
	@ npm install

# Some of the targets are inside the included ./academy-presentation-tooling/makefiles/tools.mk
install: pull-submodules update-submodules npm-install ## Install the node preqs and update submodules
	@ echo 'Installing Git hooks'
	@ npx husky install
	@ make build-scripts-compile-sass
	@ echo 'Done'

pull-submodules: ## Pull down latest submodules for first time (academy-presentation-tooling)
	@ echo 'Pulling Submodules'
	@ git submodule update --init --recursive

update-submodules: ## Update submodules to latest commit on main (academy-presentation-tooling)
	@ echo 'Updating Submodules to latest commit'
	@ git submodule update --recursive --remote
