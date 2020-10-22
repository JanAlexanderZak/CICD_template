import json

package_json_dict = {
  "pytest_description": "status_descriptions",
  "status_pytest": "5 passed | 0 failed",
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

# Does it really have to be named package.json?
with open('package.json', 'w') as outfile:
    json.dump(package_json_dict, outfile)
