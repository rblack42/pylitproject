.PHONY: all
all:    ## Run project application
python3 -m pylitproject

.PHONY: pyinit
init:	## Create Python virtual environment
	python3 -m venv _venv

.PHONY: pyreqs
reqs:	## Load Python requirements
	pip install --upgrade pip
	pip install -r requirements.txt
