.PHONY: poetry_install unit_test watch run k6_test curl_test e2e_test

poetry_install:
	poetry install

unit_test: poetry_install
	poetry run pytest --cov

watch: poetry_install
	poetry run watchfiles 'python assigner/app.py'

run: poetry_install
	poetry run python assigner/app.py

wait_for_program_load:
	for sec in $(shell seq 1 10); do sleep 1; echo $${sec}; done

k6_test:
	k6 run k6/test.js

wait_perf_test:
	make wait_for_program_load
	make k6_test

curl_test:
	curl http://localhost:8000/

wait_curl_test:
	make wait_for_program_load
	make curl_test

e2e_test: 
	make -j 2 run wait_curl_test

perf_test:
	make -j 2 run wait_perf_test