.PHONY: run install lint

install:
	poetry install

run:
	poetry run python src/ycrawler/main.py

lint:
	poetry run pylint src/ycrawler