#!/bin/sh

pytest --cov=tests/ --cov-report=html test/
mypy --config-file=src/mypy.ini src/ --html-report mypy
pylint --rcfile=src/.pylintrc src/

cmd /k
