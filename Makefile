.PHONY: check test doctor demo

check:
	python3 scripts/check.py

test:
	PYTHONPATH=src python3 -m unittest discover -s tests

doctor:
	python3 scripts/harness_doctor.py

demo:
	PYTHONPATH=src python3 -m harness_demo.cli "Cannot log in to production"
