build:
	docker build -t nlp-blockchain:dev .

lint:
	docker run --rm -v "$(shell pwd)":/pac nlp-blockchain:dev bash -c "cd /pac && flake8 . --count --show-source --statistics"

test:
	docker run --rm -v "$(shell pwd)":/pac nlp-blockchain:dev bash -c "coverage run --source=nlpchain -m pytest --disable-pytest-warnings && coverage report --omit=\"tests/*\""
