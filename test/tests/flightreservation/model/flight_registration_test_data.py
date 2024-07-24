from dataclasses import dataclass


@dataclass
class FlightReservationTestData:
    first_name: str
    last_name: str
    email: str
    password: str
    street: str
    city: str
    zip: str
    passengers_count: str
    expected_price: str
