#!/bin/sh

pytest --cov=tests --cov-report=html:tests/pytest tests
mypy --config-file=src/mypy.ini src/ --html-report tests/mypy
pylint --rcfile=src/.pylintrc src/

cmd /k
