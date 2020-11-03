""" Replaces script.bat """

import subprocess
import sys
import re
import json
import os


class RunPytestMypyPylint:
    def __init__(self, argv):
        # Run tests only
        if len(argv) == 0:
            self.output = False
            self.execute_cmd()
        if len(argv) == 1 and argv[0] == "--update":
            self.output = True
            self.pytest, self.mypy, self.pylint = self.execute_cmd()
            self.pytest_failed, self.pytest_passed, self.mypy_success, self.pylint_score = self.parse_cmd()

            package_json = {
                "pytest_description": "status_descriptions",
                "status_pytest": f"{self.pytest_passed} passed | {self.pytest_failed} failed",
                "mypy_description": "status_descriptions",
                "status_mypy": f"{self.mypy_success}",
                "pylint_description": "status_descriptions",
                "status_pylint": f"{self.pylint_score}",
                "author": "Jan Alexander Zak",
                "repository": {
                    "type": "git",
                    "url": "https://github.com/janalexanderzak"
                }
            }
            self.update_package_json(package_json)

            shieldio_dict = {
                "pytest_color": "brightgreen",
                "pytest_label": "pytest",
                "pytest_query": "status_pytest",
                "mypy_color": "brightgreen",
                "mypy_label": "mypy",
                "mypy_query": "status_mypy",
                "pylint_color": "brightgreen",
                "pylint_label": "pylint",
                "pylint_query": "status_pylint",
            }
            self.generate_shieldio_url(shieldio_dict)
        else:
            print("Too many arguments")

    def execute_cmd(self):
        pytest_output = self.check_validity_of_command(
            "pytest --cov=tests --cov-report=html:tests/pytest tests",
            output=self.output)
        mypy_output = self.check_validity_of_command(
            "mypy --config-file=tests/mypy.ini src/ --html-report /mypy",
            output=self.output)
        pylint_output = self.check_validity_of_command(
            "pylint --rcfile=tests/.pylintrc src/",
            output=self.output)
        if self.output:
            return pytest_output.stdout.decode(), mypy_output.stdout.decode(), str(pylint_output.stdout)

    @staticmethod
    def check_validity_of_command(cmd: str, output: bool) -> subprocess.CompletedProcess:
        try:
            result = subprocess.run(
                cmd,
                capture_output=output,
            )
            return result
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            print(e)

    def parse_cmd(self):
        # Pytest
        re_fail = re.search(".{3}(?:failed)", self.pytest)
        re_pass = re.search(".{3}(?:passed)", self.pytest)
        pytest_failed = int(re_fail.group()[:-6].strip()) if re_fail is not None else 0
        pytest_passed = int(re_pass.group()[:-6].strip()) if re_pass is not None else 0

        # Mypy
        mypy_success = re.search("Success", self.mypy).group().strip()

        # Pylint
        pylint_score = re.search(".{11}(?:(previous))", self.pylint).group()[:-9].strip()

        return pytest_failed, pytest_passed, mypy_success, pylint_score

    @staticmethod
    def update_package_json(package_json):
        # TODO: Does it really have to be named package.json?
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'package.json')), 'w') as out_file:
            json.dump(package_json, out_file)

    def generate_shieldio_url(self, shieldio_dict):
        # Fixed for all
        url = "https%3A%2F%2Fraw.githubusercontent.com%2FJanAlexanderZak%2Fcicd_template%2Fmaster%2Ftests%2Fpackage.json"
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'README.md')), 'r') as f:
            text = f.readlines()

        # Pytest
        shieldio_dict["pytest_color"] = "red" if self.pytest_failed >= 1 else "brightgreen"
        pytest_url = "![Build Status](https://img.shields.io/badge/dynamic/json?color={}&label={}&query={}&url={})".format(
            shieldio_dict['pytest_color'],
            shieldio_dict['pytest_label'],
            shieldio_dict['pytest_query'],
            url)
        text[text.index('pytest  \n') + 1] = f"{pytest_url}\n"

        # Mypy
        shieldio_dict["mypy_color"] = "red" if self.mypy_success != "Success" else "brightgreen"
        mypy_url = "![Build Status](https://img.shields.io/badge/dynamic/json?color={}&label={}&query={}&url={})".format(
            shieldio_dict['mypy_color'],
            shieldio_dict['mypy_label'],
            shieldio_dict['mypy_query'],
            url)
        text[text.index('mypy  \n') + 1] = f"{mypy_url}\n"

        # Pylint
        shieldio_dict["mypy_color"] = "red" if float(self.pylint_score[0:5]) < 5 else "brightgreen"
        pylint_url = "![Build Status](https://img.shields.io/badge/dynamic/json?color={}&label={}&query={}&url={})".format(
            shieldio_dict['pylint_color'],
            shieldio_dict['pylint_label'],
            shieldio_dict['pylint_query'],
            url)
        text[text.index('pylint  \n') + 1] = f"{pylint_url}\n"

        text = "".join(text)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'README.md')), 'w') as f:
            f.write(text)


if __name__ == "__main__":
    instance = RunPytestMypyPylint(sys.argv[1:])
