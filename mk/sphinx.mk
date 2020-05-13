.PHONY:	html
html:	## run Sphinx to build html pages
	cd rst && \
	sphinx-build -d _build/doctrees . ../docs
