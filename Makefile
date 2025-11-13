.PHONY: test build

test:
	@pytest

build:
	@python3 -m pip install --upgrade build
	@python3 -m build