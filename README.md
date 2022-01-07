# report
  a base hello world outline for a cli tool

  this repository uses python3.9 and click module to create 
  the cli tool

  click module is used great for a fast design 
  and well equipped to scale with a design patterns

  click handles extra features inhabitantly and offers easy to use features

  csv to dictionay conversion is handled using pandas module

  dictionary to json conversion is handled using json module

  the testing framework is pytest

# First time use 

First you need to isntall the tool from root dir

```
pip install .
```

Now you can use the tool 'report' 

```
report [path for courses.csv] [path for students.csv] [path for tests.csv] [path for marks.csv] [path for output.json]
```
try

```
report --help
```

as an example
```
report /home/dev/Documents/Example1/courses.csv /home/dev/Documents/Example1/students.csv /home/dev/Documents/Example1/tests.csv /home/dev/Documents/Example1/marks.csv /home/dev/Documents/Example1/output.json
```

# design clarifications

  This is designed under the assumption that no values in the csv files are empty, the paths/files given are valid and exist

  The error response is different from the prompt. I believe erros should have more information.
  The weights error does not completely replace the report. There is still data to be viewed/used if there are other courses with valid weights. For this reasoning I implimented the error report in a way to have the error appear at lower level if needed. Additionally I added more errors and return values to help identify issues.

  Linear search is implimented as a strategy pattern because a larger data set might need a faster searching algorithm and the strategy pattern allows for easy additions and versioning


  The Report class is created in a way so reports can be created per student for easier addition of future features.

  naming styles should follow pep 8 for readability

  doc strings should follow google for readabilty

  different import styles for testing ability, readability, and usability.
  
    in test use this form: import src.modules.module_name as foo
    in src use this form: from src.modules.module_name import ClassName

# First time use Developement
  0) Clone/fork the repo

  ```
  git clone https://github.com/FlaccidFacade/report.git
  ```


  1) Python

  Make sure python 3.9 is installed

  ```
  python3 --version
  ```

  This project is created with 3.9.9

  2) Virtual environment

  either use the specific version of python itself
  or use virtualenv and specify

  both create a venv folder in the root dir but
  virtualenv is an extra dependency that can be used if
  you choose to use a lower version of python like python2

  python:

  ```
  python3.9 -m venv venv
  ```

  3) Activate Virtual Env

  in the same folder the virtual environment was created run:

  ```
  source venv/bin/activate
  ```

  To stop the running environment run:

  ```
  deactivate
  ```

  4) Dependencies/Requirements

  The requirements.txt file holds all the needed 
  packages for this project. 
  
  This is really the development requirements as it includes 
  the testing framework

    **Note: be sure to adjust this as your project grows 
    and that your virtual environment is activated

  ```
  pip install -r dev_requirements.txt
  ```

  5) Using Cli

  This allows for modules and commands to be simultaneously
  updated and usable

  ```
  pip install -e .
  ```

  6) Testing


  To run all tests use python3 and root test directory

  without coverage:

  ```
  python3 -m pytest test/
  ```

  with coverage:

  ```
  python3 -m pytest --cov=src test/
  ```

  with coverage report:

  ```
  python3 -m pytest --cov-report xml:cov.xml --cov=src test/
  ```

  NOTE: in visual studio using pytestArgs 
  remove "--cov-report", "xml:cov.xml", "--cov=src" arguements if you with to debug tests

  testing the cli script from the click documents recommends:

  """
  To test the script, you can make a new virtualenv and then install your package:

  virtualenv venv
  . venv/bin/activate
  pip install --editable .

  Afterwards, your command should be available:

  $ yourscript
  Hello World!

  """

  But i think end2end testing is important so lets go one step further

  """
  For basic testing, Click provides the click.testing module which provides test functionality that helps you invoke command line applications and check their behavior.

  These tools should really only be used for testing as they change the entire interpreter state for simplicity and are not in any way thread-safe!
  """

  Click testing guide: https://click.palletsprojects.com/en/8.0.x/testing/?highlight=test


# Coverage

  One of the keys to faster and more effective testing is
  analyzing test cases with coverage reports

  This project uses pytest-cov (and therefore also coverage.py)
  https://github.com/pytest-dev/pytest-cov

  pytest docs for ref:
  https://docs.pytest.org/en/6.2.x/

  I like to use a visual representation for coverage report that
  maps what lines of code are covered or not with color.

  "coverage gutters" vscode extenstion creates an easy to view coverage report

  Name: Coverage Gutters
  Id: ryanluker.vscode-coverage-gutters
  Description: Display test coverage generated by lcov or xml - works with many languages
  Version: 2.8.2
  Publisher: ryanluker
  VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters



# CREDIT
  ignore file is orginally sourced from here: 
  https://github.com/muhammad-mamdouh/Django_Projects/blob/1f31e12aefb36b33474256db40a2c551882f445e/src/.gitignore
