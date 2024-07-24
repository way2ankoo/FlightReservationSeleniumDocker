from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from main.pages.base_class import BaseClass


class FlightSearch(BaseClass):
    passengers_select = (By.ID, "passengers")
    search_flight_button = (By.ID, "search-flights")

    def __init__(self, driver):
        super().__init__(driver)

    def is_at(self):
        return self.find_element(self.search_flight_button).is_displayed()

    def select_passengers(self, no_of_passengers):
        select = Select(self.find_element(self.passengers_select))
        select.select_by_value(no_of_passengers)

    def search_flight(self):
        self.click(self.search_flight_button)
