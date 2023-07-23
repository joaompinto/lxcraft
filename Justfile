test-all: install-dependencies
    python -m pytest

install-dependencies:
    pip install -r requirements-dev.txt

test:
    python -m pytest
    python -m mypy .

test-only filter:
    python -m pytest -v -s -k {{filter}}
