.PHONY: up, format, lint, test

up:
	poetry run python3 src/main.py

format:
	poetry run ruff check . --fix --exit-non-zero-on-fix
	poetry run black .

lint:
	poetry run mypy --explicit-package-bases .
	poetry run ruff check .
	poetry run black --check .

test:
	poetry run pytest tests --cov-config=.coveragerc --cov=src
