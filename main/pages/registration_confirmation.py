from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from main.base_class import BaseClass


class RegistrationConfirmation(BaseClass):
    go_to_flight_search_button = (By.ID, "go-to-flights-search")
    first_name_element = (By.CSS_SELECTOR, "#registration-confirmation-section p b")

    def __init__(self, driver):
        super().__init__(driver)

    def is_at(self):
        return self.find_element(RegistrationConfirmation.go_to_flight_search_button).is_displayed()

    def get_first_name(self):
        return self.find_element(self.first_name_element).text

    def go_to_flight_search(self):
        self.click(self.go_to_flight_search_button)


