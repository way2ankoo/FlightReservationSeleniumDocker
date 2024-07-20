import pytest

from main.pages.flight_search_page import FlightSearch
from main.pages.registration_confirmation import RegistrationConfirmation
from main.pages.registration_page import RegistrationPage


@pytest.mark.usefixtures("driver")
class TestFlightReservation:

    @pytest.mark.dependency()
    def test_user_registration(self, driver):
        self.registration_page = RegistrationPage(driver)
        self.registration_page.go_to("https://d1uh9e7cu07ukd.cloudfront.net/selenium-docker/reservation-app/index.html")
        assert self.registration_page.is_at() is True, "Registration Page not found"
        self.registration_page.enter_user_details("ankit", "rawat")
        self.registration_page.enter_user_credentials("wah@gal.com", "admin")
        self.registration_page.register()

    @pytest.mark.dependency(depends=["TestFlightReservation::test_user_registration"])
    def test_registration_confirmation(self, driver):
        self.registration_confirmation = RegistrationConfirmation(driver)
        assert self.registration_confirmation.is_at() is True, "Confirmation page not found"
        assert self.registration_confirmation.get_first_name() == "ankit", "first name not matches"
        self.registration_confirmation.go_to_flight_search()

    @pytest.mark.dependency(depends=["TestFlightReservation::test_registration_confirmation"])
    def test_flight_search(self, driver):
        self.flight_search = FlightSearch(driver)
        assert self.flight_search.is_at() is True, "Not found search flight page"
        self.flight_search.select_passengers("3")
        self.flight_search.search_flight()
