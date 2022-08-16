#----------------------
# make help
#----------------------
..DEFAULT_GOAL := help
.PHONY: help up stop down rebuild reset pull fromscratch setup install lint test deploy

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


#----------------------
# Continious Integration
#----------------------
build: install lint test
all: install lint test release deploy 

setup:  ## [setup] initialize virtualenv
	@python3 -m venv .venv
	. .venv/bin/activate

install:  ## [dependencies] install dependencies
	@pip install --upgrade pip
	@pip install -r requirements/dev.txt

lint:  ## [linter] run flake8
	@flake8 . --exclude .venv --count --select=E9,F63,F7,F82 --show-source --statistics
	@flake8 . --exclude .venv --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test: ## [tests] run unitest using pytest
	@pytest tests

format: ## [format]: run black and isort
	@black src/ tests/
	@isort src tests/

release: ## [release] applies semantic-release
	@semantic-release publish

deploy: ## [deploy]: dockerize project


#----------------------
# docker-compose
#----------------------
fromscratch: reset pull up
up: ## [docker-compose] run the project
	@docker-compose up

stop: ## [docker-compose] stop Docker containers without removing them
	@docker-compose stop

down: ## [docker-compose] stop and remove docker containers
	@docker-compose down --remove-orphans

rebuild: ## [docker-compose] rebuild base docker images
	@docker-compose down --remove-orphans
	@docker-compose build --no-cache

reset: ## [docker-compose] update docker images and reset local databases
	@docker-compose down --volumes --remove-orphans
	@docker-compose pull

pull: ## [docker-compose] update docker images without losing local databases
	@docker-compose down --remove-orphans
	@docker-compose pull
