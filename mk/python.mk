.PHONY: pyinit
pyinit:	## Create Python virtual environment
	python3 -m venv _venv

.PHONY: pyreqs
pyreqs:	## Load Python requirements
	pip install --upgrade pip
	pip install -r requirements.txt
