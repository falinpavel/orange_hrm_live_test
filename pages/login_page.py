import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")
    REQUIRED_TEXT_LOGIN = ("xpath", "(//span[text()='Required'])[1]")
    REQUIRED_TEXT_PASSWORD = ("xpath", "(//span[text()='Required'])[2]")
    INVALID_CREDENTIALS = ("xpath", "//p[text()='Invalid credentials']")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(
            self.USERNAME_FIELD)
        ).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_FIELD)
        ).send_keys(password)

    @allure.step("Click on 'Submit' button")
    def click_submit_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    @allure.step("Check required text for login")
    def check_required_text_login(self, prompt):
        self.wait.until(
            EC.text_to_be_present_in_element(self.REQUIRED_TEXT_LOGIN, prompt)
        )

    @allure.step("Check required text for password")
    def check_required_text_password(self, prompt):
        self.wait.until(
            EC.text_to_be_present_in_element(self.REQUIRED_TEXT_PASSWORD, prompt)
        )

    @allure.step("Check invalid credentials")
    def check_invalid_credentials(self, prompt):
        self.wait.until(
            EC.text_to_be_present_in_element(self.INVALID_CREDENTIALS, prompt)
        )
