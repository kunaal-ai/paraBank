# paraBank
[Parabank](https://parabank.parasoft.com/parabank/index.htm) is fully banking site. Which is being used by QA engineers to explore testing tools. This repo is development of testing framework from scratch using Python, Pytest and Playwright. Utilizing Page object models, fixtures, html reports, and running on gihub workflow. User credentials are security saved in github secrets and using plugin dotenv, to toggle password when running on cloud or local machine. 

### Structure 
```
.github
   |-- workflows
   |   |-- python-app.yml
.gitignore
.vscode
   |-- settings.json
Jenkinsfile
README.md
conftest.py
pages
   |-- __init__.py
   |-- bill_pay_page.py
   |-- helper_pom
       |-- payment_services_tab.py
   |-- home_login_page.py
   |-- overview_page.py
   |-- request_loan_page.py
pytest.ini
requirements.txt
tests
   |-- __init__.py
   |-- test_bill_pay.py
   |-- test_home_login.py
   |-- test_overview.py
   |-- test_request_loan.py
```

# How to run test
- ```pytest``` - runs the tests and report will be saved in results dir.
- ```pytest --headed``` - runs tests in headed mode.


### Parallel Test
- To run test parallel run ```pytest -n x``` x is the number of workers.(e.g 4) or use 
- ```pytest -n auto``` , which will use all possible workers automatically.

# Plugins used
- [reporter-html1-0.8.3](https://pypi.org/project/pytest-reporter-html1/) - Generate reports in html format 
- [base-url-2.0.0](https://pypi.org/project/pytest-base-url/) - provides an optional base URL via the command line or configuration file.
- [dotenv-0.5.2](https://pypi.org/project/python-dotenv/) - reads key-value pairs from a .env file and can set them as environment variables.
- [xdist-3.3.1](https://pypi.org/project/pytest-xdist/) - distributing tests across multiple CPUs to speed up test execution:
- [playwright-0.3.3](https://playwright.dev/python/)

### Other tools and version
- python 3.10.9
- pytest 7.1.2

### CI/CD
- Jenkins build gets triggered using webhook and proxy server via ngrok
- cron job schedule is set to 60 minutes.
