.DEFAULT_GOAL := help
.PHONY: serve freeze help

help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

serve:  	## Run server.
	python3 manage.py runserver

freeze: 	## Save requirements.
	pip3 freeze > requirements.txt