import datetime
import os.path

import pytest
from selenium import webdriver

from test.tests.flightreservation.model.flight_registration_test_data import FlightReservationTestData
from test.tests.vendorportal.model.vendor_portal_test_data import VendorPortalTestData
from test.util.json_util import JsonUtil


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser choice: chrome or firefox"
    )


def load_data(data_paths, data_model):
    data = []
    for path in data_paths:
        data_ = JsonUtil.load_json_to_dataclass(path, data_model)
        data.append(data_)
    return data


def load_passenger_data():
    test_data_paths = ["test\\resources\\test-data\\flightreservation\\passenger-1.json",
                       "test\\resources\\test-data\\flightreservation\\passenger-2.json",
                       "test\\resources\\test-data\\flightreservation\\passenger-3.json"]

    return load_data(test_data_paths, FlightReservationTestData)


def load_vendor_data():
    test_data_paths = ["test\\resources\\test-data\\vendorportal\\john.json",
                       "test\\resources\\test-data\\vendorportal\\mike.json",
                       "test\\resources\\test-data\\vendorportal\\sam.json"]

    return load_data(test_data_paths, VendorPortalTestData)


@pytest.fixture(scope="class", params=load_passenger_data())
def passenger_data(request):
    return request.param


@pytest.fixture(scope="class", params=load_vendor_data())
def vendor_data(request):
    return request.param


@pytest.fixture(scope="class")
# @pytest.fixture(scope="class", params=["chrome", "firefox"])
def driver(request):
    # global driver
    # for local execution
    # driver = webdriver.Chrome()

    # for remote execution Eg. selenium grid
    # browser = request.config.getoption("--browser")
    browser = request.param
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


def pytest_configure(config):
    now = datetime.datetime.now()

    now_d = now.strftime("%Y-%m-%d")
    res_dir = f'results/{now_d}'

    if not os.path.exists(res_dir):
        os.makedirs(res_dir)

    now_dt = now.strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"{res_dir}/report_{now_dt}.html"

    config.option.htmlpath = report_file


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("driver")

            now = datetime.datetime.now()
            now_d = now.strftime("%Y-%m-%d")
            res_dir = f'results/{now_d}'
            png_file = f"/{item.name}.png"

            screenshot_path = res_dir + png_file
            # file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(driver, screenshot_path)
            if screenshot_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % png_file
                extra.append(pytest_html.extras.image(screenshot_path))
        report.extra = extra


def _capture_screenshot(driver, name):
    driver.save_screenshot(name)
