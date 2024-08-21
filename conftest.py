import datetime
import os.path

import pytest
from selenium import webdriver

from test.tests.flightreservation.model.flight_registration_test_data import FlightReservationTestData
from test.tests.vendorportal.model.vendor_portal_test_data import VendorPortalTestData
from test.util.json_util import JsonUtil


# driver = None

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on (chrome or firefox)")


def load_passenger_data():
    test_data_paths = ["test\\resources\\test-data\\flightreservation\\passenger-1.json",
                       "test\\resources\\test-data\\flightreservation\\passenger-2.json",
                       "test\\resources\\test-data\\flightreservation\\passenger-3.json"]
    passengers = []
    for path in test_data_paths:
        passenger = JsonUtil.load_json_to_dataclass(path, FlightReservationTestData)
        passengers.append(passenger)
    return passengers


def load_vendor_data():
    test_data_paths_ = ["test\\resources\\test-data\\vendorportal\\john.json",
                        "test\\resources\\test-data\\vendorportal\\mike.json",
                        "test\\resources\\test-data\\vendorportal\\sam.json"]

    vendors = []
    for path_ in test_data_paths_:
        vendor = JsonUtil.load_json_to_dataclass(path_, VendorPortalTestData)
        vendors.append(vendor)
    return vendors


@pytest.fixture(scope="class", params=load_passenger_data())
def passenger_data(request):
    # test_data = JsonUtil.load_json_to_dataclass(request.param, FlightReservationTestData)
    return request.param
    # return test_data


@pytest.fixture(scope="class", params=load_vendor_data())
def vendor_data(request):
    return request.param


@pytest.fixture(scope="class")
def driver(request):
    # global driver
    # for local execution
    driver = webdriver.Chrome()

    # for remote execution Eg. selenium grid
    # browser = request.config.getoption("--browser")
    # selenium_grid_url = "http://localhost:4444/wd/hub"
    # if browser == "chrome":
    #     options = webdriver.ChromeOptions()
    # elif browser == "firefox":
    #     options = webdriver.FirefoxOptions()

    # driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)

    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_configure(config):
    if not os.path.exists('results'):
        os.makedirs('results')

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"results/report_{now}.html"

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
            screenshot_path = f"results/{item.name}.png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(driver, screenshot_path)
            if screenshot_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screenshot_path
                extra.append(pytest_html.extras.image(screenshot_path))
        report.extra = extra


def _capture_screenshot(driver, name):
    driver.save_screenshot(name)
