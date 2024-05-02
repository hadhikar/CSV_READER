run:
	python csv_reader/app.py

test:
	pytest -s --cov-report term --cov-report xml:coverage/coverage.xml --cov-report html:coverage/coverage.html --cov-config=.coveragerc --cov=csv_reader/ tests/

show_coverage:
	open coverage/coverage.html/index.html
