import random
import time
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Auth")
class TestAuth(BaseTest):

    @allure.title("Authorization user with valid credentials")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_auth_valid(self):
        """
        Тест-кейс: Авторизация пользователя с валидными данными:
        1. Открыть главную страницу (делаем скриншот)
        2. Ввести валидный логин
        3. Ввести валидный пароль
        4. Нажать на кнопку "Submit"
        5. Происходит редирект на страницу "Dashboard"
        6. Нажать на выпадающее меню "Logout"
        7. Нажать на кнопку "Выход"
        """
        self.login_page.open()
        self.login_page.make_screenshot("test_auth_valid")
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.click_logout_button()

    @allure.title("Authorization user with invalid credentials")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_auth_invalid(self):
        """
        Тест-кейс: Авторизация пользователя с невалидными данными:
        1. Открыть главную страницу (делаем скриншот)
        2. Нажать на кнопку "Submit"
        3. Проверить, что текст-подсказка "Required" для поля "Логин" появился на странице
        4. Проверить, что текст-подсказка "Required" для поля "Пароль" появился на странице
        5. Ввести невалидный логин
        6. Ввести невалидный пароль
        7. Нажать на кнопку "Submit"
        8. Проверить, что текст "Invalid credentials" появился на странице
        9. Ввести валидный логин
        10. Ввести валидный пароль
        11. Нажать на кнопку "Submit"
        12. Нажать на выпадающее меню "Logout"
        13. Нажать на кнопку "Выход"
        """
        self.login_page.open()
        self.login_page.click_submit_button()
        self.login_page.make_screenshot("test_auth_invalid")
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
