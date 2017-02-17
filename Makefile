default: develop

clean:
	find . -name '*.pyc' | xargs rm
	find . -name '*.egg-info' | xargs rm -rf

develop: clean requirements
	manage.py migrate

requirements:
	pip install --upgrade -e .
	pip install --upgrade -e .[test]

qt:
	py.test -q --reuse-db tests --tb=short

coverage:
	coverage run --source downloadcounter -m py.test -q --reuse-db --tb=short tests
	coverage report -m

lint:
	flake8 src

isort:
	isort `find . -name '*.py' -not -path '*/migrations/*'`