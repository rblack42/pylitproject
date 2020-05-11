# Makefile
PROJECT	:=	$(notdir $(PWD))

.PHONY: all
all:	## Run project application
		python3 -m pylitproject

.PHONY: init
init:	## Set up Python virtualenv
	test -d _venv || \
	python3 -m venv _venv && \
	source _venv/bin/activate && \
	pip install -U pip

.PHONY: dirs
dirs:	## Create project directories
	mkdir -p $(PROJECT)
	mkdir -p docs
	mkdir -p rst/_static
	touch docks/.nojekyll

.PHONY: reqs
reqs:	## install Python dependencies
	source _venv/bin/activate && \
	pip install -r requirements.txt

.PHONY: docs
docs:
	source _venv/bin/activate && \
	cd rst && \
	sphinx-build -b html -d _build/doctrees . ../docs
.PHONY: lint
lint:
	tox -e lint

.PHONY: test
test:
	tox
