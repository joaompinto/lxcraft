all: install-dependencies test lint

install-dependencies:
    pip install -r requirements-dev.txt

test:
    python -m pytest

lint:
    python -m mypy .
    ruff .

test-only filter:
    python -m pytest -x -v -s -k {{filter}}
