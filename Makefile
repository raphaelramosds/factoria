.PHONY: test build

test:
	@pytest

build:
	@python3 -m build

submit:
	...