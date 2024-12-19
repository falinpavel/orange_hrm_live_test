import random
import allure
from base.base_test import BaseTest


"""
Тест кейс: Авторизация пользователя. 

Gherkin:
    Scenario: Авторизация пользователя
        Given Я переходю на страницу "OrangeHRM"
        When Я нажимаю кнопку "Login" без ввода логина и пароля
        Then Я остаюсь на странице "OrangeHRM"
        And Я вижу сообщение "Required" под полями "Username"
        And Я вижу сообщение "Required" под полем "Password"
        When Я ввожу логин и пароль
        And Я нажимаю кнопку "Login"
        Then Я остаюсь на странице "OrangeHRM"
        And Я вижу сообщение "Invalid credentials"
        When Я ввожу валидные логин и пароль
        And Я нажимаю кнопку "Login"
        Then Происходит успешный вход и редирект на "Dashboard"
"""


@allure.feature("Auth")
class TestAuth(BaseTest):
    @allure.title("Authorization user")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_auth(self):
        self.login_page.open()
        self.login_page.click_submit_button()
        self.login_page.make_screenshot("test_auth")
        self.login_page.check_required_text_login("Required")
        self.login_page.check_required_text_password("Required")
        self.login_page.enter_login(f"Test {random.randint(1, 100)}")
        self.login_page.enter_password(f"Test {random.randint(1, 100)}")
        self.login_page.click_submit_button()
        self.login_page.check_invalid_credentials("Invalid credentials")
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.click_logout_button()
