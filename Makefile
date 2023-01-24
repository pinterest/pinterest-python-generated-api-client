
all: clean build ## Run all targets in this make file

clean: clean-build clean-pyc ## Clean

clean-build:				## Clean python build
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr .tox

clean-pyc:					## Clean python binaries
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

build: 						## Build command
	python -m build
	ls -l dist

build_test: 				## Build command
	IS_TEST_BUILD=1 python -m build
	ls -l dist

pip_release_install:
	pip install twine build

publish_pypi_test: clean pip_release_install build_test
	twine upload -r testpypi dist/*

publish_pypi: clean pip_release_install build
	twine upload -r pypi dist/*
