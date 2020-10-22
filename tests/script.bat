#!/bin/bat

pytest --cov=tests --cov-report=html:tests/pytest tests
mypy --config-file=tests/mypy.ini src/ --html-report tests/mypy
pylint --rcfile=tests/.pylintrc src/
pip freeze > requirements.txt
