

reload:
	pip uninstall tenant -y  && pip install --use-feature=in-tree-build .

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete