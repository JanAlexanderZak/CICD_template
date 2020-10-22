""" Replaces script.bat """

import subprocess
import os


def main():
    # Executes commands
    #x = os.system("pytest --cov=tests --cov-report=html:tests/pytest tests")
    print('#' * 80)
    #os.system("mypy --config-file=src/mypy.ini src/ --html-report tests/mypy")
    print('#' * 80)
    # os.system("pylint --rcfile=src/.pylintrc src/")
    print('#' * 80)

    # Trying to catch the output
    # subprocess.run(["cmd", "dir"], shell=True)


if __name__ == "__main__":
    main()

