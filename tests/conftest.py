from selenium import webdriver
import pytest

@pytest.fixture()
def setUp():
    print(" Running method level setup")

    yield

    print(" Running method level Tear down")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):

    print(" Running class level setup method")

    baseurl = "https://rpmsoftware.com/hiring/2020/integration-test/form-edit.html"
    if browser == 'chrome':
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)


    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

    elif browser == 'ie':
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

    elif browser == 'safari':
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

    else:

        # if no specific browser is given on command line it will rum on chrome By default

        driver = webdriver.Chrome()
        baseurl = "https://rpmsoftware.com/hiring/2020/integration-test/form-edit.html"
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

    # means if the class attribute we are getting request from is not None
    if request.cls is not None:
        # then this value will be avilable to complete class instance
        request.cls.driver = driver


    # this will return value to the place where this OneTimeSetUp fixture is used
    yield driver
    driver.quit()
    print(" Running class level Teardown")


# parser method pytest_addoption is an internal pytest implementation
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--OSType", help="Type os type")

# nOw create a fixture to use
@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")





