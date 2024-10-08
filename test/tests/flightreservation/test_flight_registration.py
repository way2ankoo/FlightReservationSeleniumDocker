import pytest

from main.pages.flightreservation.flight_search_page import FlightSearch
from main.pages.flightreservation.registration_confirmation import RegistrationConfirmation
from main.pages.flightreservation.registration_page import RegistrationPage


@pytest.mark.usefixtures("driver", "passenger_data")
class TestFlightReservation:

    # @pytest.mark.dependency()
    def test_user_registration(self, driver, passenger_data):
        self.registration_page = RegistrationPage(driver)
        self.registration_page.go_to("https://d1uh9e7cu07ukd.cloudfront.net/selenium-docker/reservation-app/index.html")
        assert self.registration_page.is_at() is True, "Registration Page not found"
        self.registration_page.enter_user_details(passenger_data.first_name, passenger_data.last_name)
        self.registration_page.enter_user_credentials(passenger_data.email, passenger_data.password)
        self.registration_page.register()

    # @pytest.mark.dependency(depends=["TestFlightReservation::test_user_registration"])
    def test_registration_confirmation(self, driver, passenger_data):
        self.registration_confirmation = RegistrationConfirmation(driver)
        assert self.registration_confirmation.is_at() is True, "Confirmation page not found"
        assert self.registration_confirmation.get_first_name() == passenger_data.first_name, "first name not matches"
        self.registration_confirmation.go_to_flight_search()

    # @pytest.mark.dependency(depends=["TestFlightReservation::test_registration_confirmation"])
    def test_flight_search(self, driver, passenger_data):
        self.flight_search = FlightSearch(driver)
        assert self.flight_search.is_at() is True, "Not found search flight page"
        self.flight_search.select_passengers(passenger_data.passengers_count)
        self.flight_search.search_flight()
