import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome(r"C:\Users\Administrator\arcserveui_project\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    driver.implicitly_wait(20)
    return driver
    driver.close()


#This function will get the value from cli
def pytest_addoption(parser):
    parser.addoption('--browser')

#This will return the value to the setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

