SHELL:=bash
OPENAPI_GENERATOR_VERSION:=5.4.0
OPENAPI_GENERATOR_COMMAND:=local-openapi-generator-cli

# Additional debugging output can be enabled by setting e.g. DEBUG_MODELS=1.
ifeq ($(DEBUG_MODELS),1)
GENERATOR_FLAGS += --global-property debugModels=true
endif
ifeq ($(DEBUG_OPS),1)
GENERATOR_FLAGS += --global-property debugOperations=true
endif

all: download_spec validate_spec generate_client patch_client ## General external client

download_spec:						## Download openapi.yaml from public pinterest github repo
	@echo ====Download openapi.yaml from public pinterest github repo====
	python utils/download_file.py https://raw.githubusercontent.com/pinterest/api-description/main/v5/openapi.yaml  './openapi.yaml'

validate_spec: 						## Validates the openapi spec: sdk.yaml
	@echo ====Validates the openapi spec: sdk.yaml====
	./local-open-generator-cli validate -i openapi.yaml

generate_client:			## Generates a python client
	@echo ====Generates a python client using the sdk.yaml spec====
	./local-open-generator-cli generate -c config.yml -o ..
	rm -rf ../test ../.gitlab-ci.yml ../.travis.yml ../git_push.sh

patch_client:			## Patch the generated client
	@echo ====Executing patches====
	python ./patches/remove_bool_none_type.py
	python ./patches/fix_urllib3_deprecations.py

help:								## Show list of targets and purposes.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'