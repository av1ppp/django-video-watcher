.DEFAULT_GOAL := help
.PHONY: serve freeze help install clean

DB_NAME = csrweb
DB_USERNAME = ceaser
DB_PASSWORD = 0905


help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

serve:		## Run server.
	python3 manage.py runserver 8888

freeze:		## Save requirements.
	pip3 freeze > requirements.txt

install:    ## Install packages.
	sudo apt install -y libmysqlclient-dev default-libmysqlclient-dev python3-dev mysql-server mysql-client

	sudo mysql --execute="CREATE USER IF NOT EXISTS '$(DB_USERNAME)'@'%' IDENTIFIED BY '$(DB_PASSWORD)';"
	sudo mysql --execute="GRANT ALL PRIVILEGES ON *.* TO '$(DB_USERNAME)'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;"
	sudo mysql --execute="CREATE DATABASE IF NOT EXISTS $(DB_NAME)"

	python -m pip install --upgrade pip
	pip3 install -r requirements.txt

	./manage.py migrate

clean:      ## Clean byte-compiled files.
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +
	find . -name '__pycache__' -type d -exec rm -rf  {} +