.PHONY: poetry_install unit_test watch run k6_test curl_test e2e_test

poetry_install:
	poetry install

unit_test: poetry_install
	poetry run pytest --cov

watch: poetry_install
	poetry run watchfiles 'python assigner/app.py'

run: poetry_install
	poetry run python assigner/app.py

k6_test:
	k6 run k6/test.js

curl_test:
	for sec in $(shell seq 1 10); do sleep 1; echo $${sec}; done
	curl http://localhost:8000/

e2e_test: 
	make -j 2 run curl_test
