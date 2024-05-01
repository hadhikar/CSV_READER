run:
	python app.py

test:
	pytest --cov=./ --cov-report html:coverage/

coverage:
	open coverage/index.html
