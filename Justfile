test-all: install-dependencies
    python -m pytest

install-dependencies:
    pip install -r requirements-dev.txt

test:
    python -m pytest -x
    python -m mypy .

test-only filter:
    python -m pytest -x -v -s -k {{filter}}
