.PHONY: test build install clean publish

PACKAGE_NAME := factoria
VERSION := 0.1.0
DIST_DIR := dist
WHEEL_FILE := $(DIST_DIR)/$(PACKAGE_NAME)-$(VERSION)-py3-none-any.whl

test:
	@pytest -v --maxfail=1 --disable-warnings

build: clean
	@echo "Building package..."
	@python3 -m build

install: $(WHEEL_FILE)
	@echo "Installing package..."
	@pip install $(WHEEL_FILE)

clean:
	@echo "Cleaning build artifacts..."
	@rm -rf $(DIST_DIR) build *.egg-info

publish: build
	@echo "Publishing to PyPI..."
	@twine upload $(DIST_DIR)/*
