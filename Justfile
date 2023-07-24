all: install-dependencies test

install-dependencies:
    pip install -r requirements-dev.txt

test:
    python -m pytest -x

test-only filter:
    python -m pytest -x -v -s -k {{filter}}

coverage:
    python -m pytest -x --cov-report term-missing --cov=lxcraft tests

coverage-only filter:
    python -m pytest -x --cov-report term-missing --cov=lxcraft tests -k {{filter}}

lint:
    python -m mypy .
    ruff .
