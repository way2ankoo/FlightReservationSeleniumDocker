from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from main.pages.base_class import BaseClass


class DashboardPage(BaseClass):

    monthly_earnings_element = (By.ID, "monthly-earning")

    annual_earnings_element = (By.ID, "annual-earning")

    profit_margin_element = (By.ID, "profit-margin")

    available_inventory_element = (By.ID, "available-inventory")

    search_input = (By.CSS_SELECTOR, "#dataTable_filter input")

    search_results_count_element = (By.ID, "dataTable_info")

    user_profile_picture_element = (By.CSS_SELECTOR, "img.img-profile ")

    logout_link = (By.LINK_TEXT, "Logout")

    logout_modal_button = (By.CSS_SELECTOR, "#logoutModal a")

    def __init__(self, driver):
        super().__init__(driver)

    def is_at(self):
        monthly_earnings = self.wait.until(EC.visibility_of_element_located(DashboardPage.monthly_earnings_element))
        return monthly_earnings.is_displayed()

    def get_monthly_earnings(self):
        return self.find_element(self.monthly_earnings_element).text

    def get_annual_earnings(self):
        return self.find_element(self.annual_earnings_element).text

    def get_profit_margin(self):
        return self.find_element(self.profit_margin_element).text

    def get_available_inventory(self):
        return self.find_element(self.available_inventory_element).text

    def search_order_history(self, keyword):
        self.type(keyword, self.search_input)

    def get_search_results_count(self):
        result_text = self.find_element(self.search_results_count_element).text
        arr = result_text.split(" ")
        count = int(arr[5])
        print(f"Result count: {count}")
        return count

    def logout(self):
        self.click(self.user_profile_picture_element)
        self.wait.until(EC.visibility_of_element_located(self.logout_link))
        self.click(self.logout_link)

        self.wait.until(EC.visibility_of_element_located(self.logout_modal_button))
        self.click(self.logout_modal_button)


