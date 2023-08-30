poetry_install:
	poetry install

unit_test: poetry_install
	poetry run pytest --cov

run: poetry_install
	poetry run watchfiles 'python assigner/app.py'
