test-all: install-dependencies
    python -m pytest

install-dependencies:
    pip install -r requirements-dev.txt
