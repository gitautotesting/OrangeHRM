import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('Launching Chrome browser')
    elif browser == 'edge':
        driver = webdriver.Edge()
        print('launching Edge browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('Launching Firefox browser')
    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('Headless')
        driver = webdriver.Chrome(options=chrome_option)
        print('Headless Mode')
    return driver


# ==================== pytest html reports ========================

# **************** To add Additional details in the html report (Environment Section)***********************

def pytest_metadata(metadata):
    metadata['Environment'] = 'Test'
    metadata['Project Name'] = 'OrangeHRM'
    metadata['Module name'] = 'Customer'
    metadata['Tester'] = 'Shubham'

# *************** To remove unwanted data from html report (Environment Section) **************************
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
