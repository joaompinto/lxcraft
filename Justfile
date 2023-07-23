test: install-dependencies
    python -m pytest
    python -m mypy .

install-dependencies:
    pip install -r requirements-dev.txt

test-only filter:
    python -m pytest -x -v -s -k {{filter}}
