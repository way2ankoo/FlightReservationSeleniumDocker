from dataclasses import dataclass


@dataclass
class VendorPortalTestData:
    username: str
    password: str
    monthlyEarning: str
    annualEarning: str
    profitMargin: str
    availableInventory: str
    searchKeyword: str
    searchResultsCount: int
