.PHONY: install test lint clean

install:
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache build dist *.egg-info
