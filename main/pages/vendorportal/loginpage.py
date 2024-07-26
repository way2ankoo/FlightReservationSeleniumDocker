from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from main.pages.base_class import BaseClass


class LoginPage(BaseClass):

    username_input = (By.ID, "username")

    password_input = (By.ID, "password")

    login_button = (By.ID, "login")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to(self, url):
        self.driver.get(url)

    def is_at(self):
        username_field = self.wait.until(EC.visibility_of_element_located(LoginPage.username_input))
        return username_field.is_displayed()

    def login(self, username, password):
        self.type(username, LoginPage.username_input)
        self.type(password, LoginPage.password_input)
        self.click(LoginPage.login_button)
