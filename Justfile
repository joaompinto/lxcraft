all: install-dependencies test

install-dependencies:
    pip install -r requirements-dev.txt

test:

lint:
    python -m mypy .
    ruff .

test-only filter:
    python -m pytest -x -v -s -k {{filter}}
