import json


def executable():
    # api to return current values for mypy pytest...
    pass


def generate_dict():
    pass


def generate_files():
    with open("README.md", 'r') as f:
        text = f.readlines()
        print(text)


    pass


package_json_dict = {
  "pytest_description": "status_descriptions",
  "status_pytest": "5 passed | 0 failed",
  "pytest-cov_description": "status_descriptions",
  "status_pytest-cov": "100%",
  "mypy_description": "status_descriptions",
  "status_mypy": "success",
  "pylint_description": "status_descriptions",
  "status_pylint": "10.0 / 10",
  "author": "Jan Alexander Zak",
  "repository": {
    "type": "git",
    "url": "https://github.com/vemarav/subdomains"
  }
}

# TODO:
# Get current result from subprocess and fill in
# alter green / red

# paste url in readme here

# Does it really have to be named package.json?
with open('package.json', 'w') as outfile:
    json.dump(package_json_dict, outfile)
