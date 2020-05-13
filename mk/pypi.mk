.PHONY: build
build:	inc_build	## bump build and package project for PyPi
	python setup.py sdist bdist_wheel
	twine check list/*

.PHONY: pypitest
pypitest:	## Upload project to PyPi test site
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: upload
upload:	## Upload new version to PyPi
	twine upload dist/*
