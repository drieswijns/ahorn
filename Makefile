all:
	pip install -r requirements.txt
	python setup.py install

test: all
	python -m pytest tests
