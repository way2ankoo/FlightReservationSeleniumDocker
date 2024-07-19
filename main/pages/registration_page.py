from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from main.base_class import BaseClass


class RegistrationPage(BaseClass):
    first_name_input = (By.ID, "firstName")
    last_name_input = (By.ID, "lastName")
    email_input = (By.ID, "email")
    password_input = (By.ID, "password")
    register_button = (By.ID, "register-btn")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_user_details(self, first_name, last_name):
        self.type(first_name, RegistrationPage.first_name_input)
        self.type(last_name, RegistrationPage.last_name_input)

    def enter_user_credentials(self, email, password):
        self.type(email, RegistrationPage.email_input)
        self.type(password, RegistrationPage.password_input)

    def register(self):
        self.click(RegistrationPage.register_button)

    def is_at(self):
        # self.wait.until(EC.visibility_of_element_located(RegistrationPage.first_name_input))
        return self.find_element(RegistrationPage.first_name_input).is_displayed()

    def go_to(self, url):
        self.driver.get(url)




