# Code Coverage and Test Coverage Using Pytest

`Step 1. Unittest` \
`Step 2. Pytest` \
`Step 3. Code Coverage` \
`Step 4. Test Coverage`

```
*******************unittest*************

to run unittests
if __name__ == "__main__":
        unittest.main()
        
******************pytest****************pip install pytest        

install pytest and  remove the if __name__ above method  and type pytest to run all tests.

pytest       -> run all the tests
pytest -v    -> run all the tests with more details

****************code coverage************ pip install coverage

coverage run app.py
coverage report
coverage report -m (implicit command for details)
coverage report --show-missing (explicit command for details)

to write coverage report to xml and html
coverage xml
coverage html

****************test coverage************ pip install pytest-cov

pytest --cov=src
pytest -v --cov=src
pytest -v --cov=src --cov-report=html
pytest -v --cov=src --cov-report=xml

Test code and save reports to the selected directory

pytest --cov=src --cov-report=html:coverage-reports/htmlcov --cov-report=xml:coverage-reports/coverage.xml

************* Tests Paths**************
sys.path.append("../")