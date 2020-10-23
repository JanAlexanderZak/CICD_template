""" Replaces script.bat """

import subprocess
import os
import sys
import re
import json


class PytestMypyPylintExecutable:
    def __init__(self, argv):
        if len(argv) == 0:
            self.output = False
            self.execute_cmd()
        if len(argv) == 1 and argv[0] == "--update":
            self.output = True
            self.generate_shieldio_url()
            self.update_package_json()
        else:
            print("Too many arguments")

    def parse_cmd(self):
        pytest, mypy, pylint = self.execute_cmd()

        # Pytest
        pytest_failed = int(re.search(".{3}(?:failed)", pytest).group()[:-6].strip())
        pytest_passed = int(re.search(".{3}(?:passed)", pytest).group()[:-6].strip())
        print("Pytest failed: ", pytest_failed)
        print("Pytest passed: ", pytest_passed)

        # Mypy
        mypy_success = re.search("Success", mypy).group().strip()
        print("Mypy success: ", mypy_success)

        # Pylint
        pylint_score = re.search(".{11}(?:(previous))", pylint).group()[:-9].strip()
        print("pylint score: ", pylint_score)

        return pytest_failed, pytest_passed, mypy_success, pylint_score

    def update_package_json(self):
        pytest_failed, pytest_passed, mypy_success, pylint_score = self.parse_cmd()

        package_json_dict = {
            "pytest_description": "status_descriptions",
            "status_pytest": f"{pytest_passed} passed | {pytest_failed} failed",
            "mypy_description": "status_descriptions",
            "status_mypy": f"{mypy_success}",
            "pylint_description": "status_descriptions",
            "status_pylint": f"{pylint_score}",
            "author": "Jan Alexander Zak",
            "repository": {
                "type": "git",
                "url": "https://github.com/janalexanderzak"
            }
        }

        # TODO: Does it really have to be named package.json?
        with open('tests/package.json', 'w') as out_file:
            json.dump(package_json_dict, out_file)

    def generate_shieldio_url(self):
        # Fixed for all
        url = "https%3A%2F%2Fraw.githubusercontent.com%2FJanAlexanderZak%2Fneural_network%2Fmaster%2Ftests%2Fpackage.json"
        pytest_failed, pytest_passed, mypy_success, pylint_score = self.parse_cmd()
        print(pytest_failed)
        # Pytest
        if pytest_failed >= 1:
            pytest_color = "red"
        else:
            pytest_color = "brightgreen"
        pytest_label = "pytest"
        pytest_query = "status_pytest"
        pytest_url = f"![Build Status](https://img.shields.io/badge/dynamic/json?color={pytest_color}&label={pytest_label}&query={pytest_query}&url={url})"

        if mypy_success != "Success":
            mypy_color = "red"
        else:
            mypy_color = "brightgreen"
        mypy_label = "pylint"
        mypy_query = "status_pylint"
        mypy_url = f"![Build Status](https://img.shields.io/badge/dynamic/json?color={mypy_color}&label={mypy_label}&query={mypy_query}&url={url})"


        # Pylint
        if float(pylint_score[0:5]) < 5:
            pylint_color = "red"
        else:
            pylint_color = "red"
        pylint_label = "pylint"
        pylint_query = "status_pylint"
        pylint_url = f"![Build Status](https://img.shields.io/badge/dynamic/json?color={pylint_color}&label={pylint_label}&query={pylint_query}&url={url})"

        with open("README.md", 'r') as f:
            text = f.readlines()

        text[text.index('pytest  \n') + 1] = f"{pytest_url}\n"
        text[text.index('mypy  \n') + 1] = f"{mypy_url}\n"
        text[text.index('pylint  \n') + 1] = f"{pylint_url}\n"
        text = "".join(text)

        with open("README.md", 'w') as f:
            f.write(text)

    def update_badge(self):
        pass

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

    def execute_cmd(self):
        pytest_output = self.check_validity_of_command("pytest --cov=tests --cov-report=html:tests/pytest tests", output=self.output)
        mypy_output = self.check_validity_of_command("mypy --config-file=tests/mypy.ini src/ --html-report tests/mypy", output=self.output)
        pylint_output = self.check_validity_of_command("pylint --rcfile=tests/.pylintrc src/", output=self.output)

        if self.output:
            return pytest_output.stdout.decode(), mypy_output.stdout.decode(), str(pylint_output.stdout)


if __name__ == "__main__":
    instance = PytestMypyPylintExecutable(sys.argv[1:])
