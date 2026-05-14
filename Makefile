.PHONY: check syntax lint doctor docs test smoke demo

check:
	python3 scripts/check.py

syntax:
	python3 scripts/check_syntax.py

lint:
	python3 scripts/lint.py

doctor:
	python3 scripts/harness_doctor.py

docs:
	python3 scripts/check_docs.py

test:
	python3 scripts/check_tests.py

smoke:
	python3 scripts/check_smoke.py

demo:
	PYTHONPATH=src python3 -m harness_demo.cli "Cannot log in to production"
