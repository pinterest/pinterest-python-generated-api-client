all: pip_integration_test integration_tests

pip_integration_test:
	@echo pip install
	pip install -r requirements.txt

integration_tests:
	@echo integration tests...
	python -m pytest .