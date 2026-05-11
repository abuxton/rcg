.DEFAULT_GOAL := help

BUNDLER_VERSION ?= 2.5.23
BUNDLE := bundle _$(BUNDLER_VERSION)_

.PHONY: help bootstrap build serve clean test

help:
	@echo "Available tasks:"
	@echo "  make help      Show this help text"
	@echo "  make bootstrap Install compatible Bundler"
	@echo "  make build     Install gems and build the site"
	@echo "  make serve     Install gems and run local server with live reload"
	@echo "  make clean     Remove generated site artifacts"
	@echo "  make test      Validate Makefile workflow (help + build)"

bootstrap:
	gem install bundler -v $(BUNDLER_VERSION) --no-document

build: bootstrap
	$(BUNDLE) install
	$(BUNDLE) exec jekyll build

serve: bootstrap
	$(BUNDLE) install
	$(BUNDLE) exec jekyll serve --livereload

clean:
	rm -rf _site .jekyll-metadata

test:
	$(MAKE) help
	$(MAKE) build
