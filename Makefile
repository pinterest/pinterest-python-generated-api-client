
all: clean sdist ## Run all targets in this make file

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

sdist: 						## Build command
	python setup.py sdist
	ls -l dist