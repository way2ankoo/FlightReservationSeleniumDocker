from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(*locator))

    def find_elements(self, *locator):
        return self.wait.until(EC.visibility_of_all_elements_located(*locator))

    def click(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def type(self, text, *locator):
        element = self.find_element(*locator)
        element.send_keys(text)


