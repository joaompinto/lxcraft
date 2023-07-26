all: install-dependencies test

install-dependencies:
    pip install -r requirements-dev.txt

test: lint
    python -m pytest -x

test-only filter:
    python -m pytest -x -v -s -k {{filter}}

cover:
    python -m pytest -x --cov-report term-missing --cov=lxcraft tests

cover-only filter:
    python -m pytest -x --cov-report term-missing --cov=lxcraft tests -k {{filter}}

lint:
    python -m mypy .
    ruff .
