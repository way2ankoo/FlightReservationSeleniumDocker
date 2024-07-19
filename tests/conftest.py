import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on (chrome or firefox)")


@pytest.fixture(scope="class")
def driver(request):
    # for local execution
    # driver = webdriver.Chrome()

    # for remote execution Eg. selenium grid
    browser = request.config.getoption("--browser")
    selenium_grid_url = "http://localhost:4444/wd/hub"
    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

    driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)

    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
