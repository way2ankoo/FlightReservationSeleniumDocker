import pytest

from main.pages.vendorportal.dashboardpage import DashboardPage
from main.pages.vendorportal.loginpage import LoginPage


@pytest.mark.usefixtures("driver", "vendor_data")
class TestVendorPortal:

    @pytest.fixture(autouse=True)
    def setup(self, driver, vendor_data):
        self.driver = driver
        self.vendor_data = vendor_data
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)

    def test_login(self):
        self.login_page.go_to("https://d1uh9e7cu07ukd.cloudfront.net/selenium-docker/vendor-app/index.html")
        assert self.login_page.is_at() is True, "Login page not found"
        self.login_page.login(self.vendor_data.username, self.vendor_data.password)

    def test_dashboard(self):
        assert self.dashboard_page.is_at() is True, "Dashboard page not found"

        # assert finance metrics
        assert self.dashboard_page.get_monthly_earnings() == self.vendor_data.monthlyEarning, ("Monthly earnings data is not matching")
        assert self.dashboard_page.get_annual_earnings() == self.vendor_data.annualEarning, "Annual earnings not matching"
        assert self.dashboard_page.get_profit_margin() == self.vendor_data.profitMargin, "Profit margin is not equal"
        assert self.dashboard_page.get_available_inventory() == self.vendor_data.availableInventory, ("Available inventory mismatch")

        # assert order history
        self.dashboard_page.search_order_history(self.vendor_data.searchKeyword)
        assert self.dashboard_page.get_search_results_count() == self.vendor_data.searchResultsCount, "result count mismatch"

    def test_logout(self):
        self.dashboard_page.logout()
        assert self.login_page.is_at() is True, "login page not found lastly"
