import time
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
    PROFILE_DROPDOWN = ("xpath", "//p[@class='oxd-userdropdown-name']")
    LOGOUT_BUTTON = ("xpath", "//a[normalize-space()='Logout']")

    def enter_login(self, login):
        with allure.step("Enter login"):
            self.wait.until(EC.element_to_be_clickable(
                self.USERNAME_FIELD)
            ).send_keys(login)
            time.sleep(1)
            assert self.driver.find_element(
                *self.USERNAME_FIELD
            ).get_attribute("value") == login

    def enter_password(self, password):
        with allure.step("Enter password"):
            self.wait.until(
                EC.element_to_be_clickable(self.PASSWORD_FIELD)
            ).send_keys(password)
            time.sleep(1)
            assert self.driver.find_element(
                *self.PASSWORD_FIELD
            ).get_attribute("value") == password

    def click_submit_button(self):
        with allure.step("Click on 'Submit' button"):
            self.wait.until(
                EC.element_to_be_clickable(self.LOGIN_BUTTON)
            ).click()

    def check_required_text_login(self, prompt):
        with allure.step("Check required text for login"):
            """
            Проверка, соответствует ли подсказка пароля требованиям.
    
            :param prompt: Ожидаемая подсказка текста.
            :raises ValueError: Если текст не соответствует требованиям.
            """
            valid_prompts = ["Required", "Requis"]  # Допустимые значения
            if prompt not in valid_prompts:
                raise ValueError(f"Недопустимая подсказка: {prompt}. Ожидались: {valid_prompts}")
            try:
                self.wait.until(
                    EC.text_to_be_present_in_element(self.REQUIRED_TEXT_LOGIN, prompt)
                )
            except TimeoutError:
                raise TimeoutError(
                    f"Текст '{prompt}' не появился на странице в течение времени ожидания."
                )

    def check_required_text_password(self, prompt):
        with allure.step("Check required text for password"):
            """
            Проверка, соответствует ли подсказка пароля требованиям.
    
            :param prompt: Ожидаемая подсказка текста.
            :raises ValueError: Если текст не соответствует требованиям.
            :raises TimeoutError: Если текст не появился на странице в течение времени ожидания.
            """
            valid_prompts = ["Required", "Requis"]  # Допустимые значения
            if prompt not in valid_prompts:
                raise ValueError(f"Недопустимая подсказка: {prompt}. Ожидались: {valid_prompts}")
            try:
                self.wait.until(
                    EC.text_to_be_present_in_element(self.REQUIRED_TEXT_PASSWORD, prompt)
                )
            except TimeoutError:
                raise TimeoutError(
                    f"Текст '{prompt}' не появился на странице в течение времени ожидания."
                )

    def check_invalid_credentials(self, prompt):
        with allure.step("Check invalid credentials"):
            self.wait.until(
                EC.text_to_be_present_in_element(self.INVALID_CREDENTIALS, prompt)
            )
            assert self.driver.find_element(*self.INVALID_CREDENTIALS).text == prompt

    def click_logout_button(self):
        with allure.step("Click on 'Logout' button"):
            self.wait.until(
                EC.element_to_be_clickable(self.PROFILE_DROPDOWN)
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(self.LOGOUT_BUTTON)
            ).click()
