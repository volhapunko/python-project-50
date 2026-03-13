lint:
	uv run ruff check

lint-fix:
	uv run ruff check-fix

install:
	uv pip install -e .

check: lint test

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml