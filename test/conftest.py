import pytest
from selenium import webdriver

@pytest.yield_fixture()

def setuUp():
    print("Running method level set up")
    yield
    print("Running method level tearDown)")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(browser):
    print("Running one time setUp")
    if browser=='firefox':
        print("Running tests on FF")
    else:
        print("Running tests on Chrome")
    yield
    print("Running one time tear down")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operation system")

@pytest_fixtute(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")