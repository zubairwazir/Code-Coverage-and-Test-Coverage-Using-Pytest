# Code Coverage and Test Coverage Using Pytest

Step 1. Unittest
Step 2. Pytest
Step 3. Code Coverage
Step 4. Test Coverage

```
*******************unittest*************

to run unittests
if __name__ == "__main__":
        unittest.main()
        
        
******************pytest****************pip install pytest        
install pytest and just remove the if __name__ method and type pytest it will run all tests.

pytest       -> run all the tests
pytest -v    -> run all the tests with more details


****************code coverage************pip install coverage
coverage run app.py
coverage report
coverage report -m (implicit command for details)
coverage report --show-missing (explicit command for details)

to write coverage report to xml and html
coverage xml
coverage html


****************test coverage************pip install pytest-cov
pytest --cov=app
pytest -v --cov=app
pytest -v --cov=app --cov-report=html
pytest -v --cov=app --cov-report=xml
