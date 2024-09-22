.PHONY: install test

install:
	pip install .\[testing\] --use-pep517

test:
	pytest