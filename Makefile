.DEFAULT_GOAL := help
.PHONY: serve freeze help install clean

help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

serve:		## Run server.
	python3 manage.py runserver

freeze:		## Save requirements.
	pip3 freeze > requirements.txt

install:    ## Install packages.
	pip3 install -r requirements.txt

clean:      ## Clean byte-compiled files.
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +
	find . -name '__pycache__' -type d -exec rm -rf  {} +