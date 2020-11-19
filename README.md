travis  
[![Build Status](https://travis-ci.com/JanAlexanderZak/cicd_template.svg?branch=master)](https://travis-ci.com/JanAlexanderZak/neural_network)


pytest  
![Build Status](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=pytest&query=status_pytest&url=https%3A%2F%2Fraw.githubusercontent.com%2FJanAlexanderZak%2Fcicd_template%2Fmaster%2Ftests%2Fpackage.json)


mypy  
![Build Status](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=mypy&query=status_mypy&url=https%3A%2F%2Fraw.githubusercontent.com%2FJanAlexanderZak%2Fcicd_template%2Fmaster%2Ftests%2Fpackage.json)


pylint  
![Build Status](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=pylint&query=status_pylint&url=https%3A%2F%2Fraw.githubusercontent.com%2FJanAlexanderZak%2Fcicd_template%2Fmaster%2Ftests%2Fpackage.json)


# CICD template

<details>

## Table of contents
* [Folder Structure](#folder-structure)


</details>

## Summary
The project will be located in ./src and any tests in ./tests.  
Configuration files for tests are located in ./tests.  
Badges update automatically after running ./tests/script.py --update.  

## Folder structure
```markdown
.  
+-- src
|   +-- main.py  
+-- tests  
|   +-- mypy.ini  
|   +-- package.json 
|   +-- pytest.ini  
|   +-- requirements.txt  
|   +-- script.bat  
|   +-- script.py  
|   +-- test_main.py  
+-- .gitignore  
+-- .travis.yml  
+-- README.md  
+-- requirements.txt  
```
