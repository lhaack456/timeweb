PYTHON = python
FLASK_APP = app.py

setup:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__ *.pyc

test:
	pytest test_app.py

run:
	@$(PYTHON) $(FLASK_APP)
