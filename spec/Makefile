SHELL:=bash
OPENAPI_GENERATOR_VERSION:=5.4.0
OPENAPI_GENERATOR_COMMAND:=openapi-generator-cli

ifeq (, $(shell which $(OPENAPI_GENERATOR_COMMAND)))
OPENAPI_GENERATOR_COMMAND = openapi-generator
endif

ifeq (, $(shell which $(OPENAPI_GENERATOR_COMMAND)))
$(error Error: Command '$(OPENAPI_GENERATOR_COMMAND)' not found, make sure 'openapi-generator' is installed globablly)
endif

ifneq ($(shell OPENAPI_GENERATOR_VERSION=$(OPENAPI_GENERATOR_VERSION) $(OPENAPI_GENERATOR_COMMAND) version), $(OPENAPI_GENERATOR_VERSION))
$(error Error: Expected $(OPENAPI_GENERATOR_COMMAND) version $(OPENAPI_GENERATOR_VERSION) (found $(shell $(OPENAPI_GENERATOR_COMMAND) version)))
endif

# Additional debugging output can be enabled by setting e.g. DEBUG_MODELS=1.
ifeq ($(DEBUG_MODELS),1)
GENERATOR_FLAGS += --global-property debugModels=true
endif
ifeq ($(DEBUG_OPS),1)
GENERATOR_FLAGS += --global-property debugOperations=true
endif

all: download_spec validate_spec generate_client  ## General external client

download_spec:						## Download openapi.yaml from public pinterest github repo
	@echo ====Download openapi.yaml from public pinterest github repo====
	python utils/download_file.py  https://raw.githubusercontent.com/pinterest/api-description/main/v5/openapi.yaml  './openapi.yaml'

validate_spec: 						## Validates the openapi spec: sdk.yaml
	@echo ====Validates the openapi spec: sdk.yaml====
	openapi-generator validate -i openapi.yaml

generate_client:			## Generates a python client internal
	@echo ====Generates a python client using the sdk.yaml spec====
	openapi-generator generate -c config.yml -o ..
	rm -rf ../test ../.gitlab-ci.yml ../.travis.yml ../git_push.sh

help:								## Show list of targets and purposes.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'