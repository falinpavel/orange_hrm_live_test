import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Admin page")
class TestAdminPage(BaseTest):
    @allure.title("Check admin page and create user admin, status = enabled")
    @allure.severity("Major")
    @pytest.mark.smoke
    def test_create_user_admin(self):
        """
        Тест-кейс: Проверка страницы администратора
        1. Открыть главную страницу
        2. Ввести валидный логин
        3. Ввести валидный пароль
        4. Нажать на кнопку "Submit"
        5. Нажать на ссылку "Admin"
        6. Проверить, что открылась страница администратора
        7. Нажать на кнопку "Add"
        8. В разделе "Add User" в выпадающем списке "User Role" выбрать "Admin"
        9. В разделе "Add User" в поле ввода "Employee Name" ввести валидное значение
        10. В разделе "Add User" в выпадающем списке "Status" выбрать "Enabled"
        11. В разделе "Add User" в поле ввода "Username" ввести валидное значение
        12. В разделе "Add User" в поле ввода "Password" ввести валидное значение
        13. В разделе "Add User" в поле ввода "Confirm Password" ввести валидное значение из шага 12
        14. Нажать на кнопку "Save"
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.admin_page.click_admin_link()

    @allure.title("Check admin page and create user ESS, status = disabled")
    @allure.severity("Major")
    @pytest.mark.smoke
    def test_create_user_ess(self):
        """
        Тест-кейс: Проверка страницы администратора
        1. Открыть главную страницу
        2. Ввести валидный логин
        3. Ввести валидный пароль
        4. Нажать на кнопку "Submit"
        5. Нажать на ссылку "Admin"
        6. Проверить, что открылась страница администратора
        7. Нажать на кнопку "Add"
        8. В разделе "Add User" в выпадающем списке "User Role" выбрать "ESS"
        9. В разделе "Add User" в поле ввода "Employee Name" ввести валидное значение
        10. В разделе "Add User" в выпадающем списке "Status" выбрать "Disabled"
        11. В разделе "Add User" в поле ввода "Username" ввести валидное значение
        12. В разделе "Add User" в поле ввода "Password" ввести валидное значение
        13. В разделе "Add User" в поле ввода "Confirm Password" ввести валидное значение из шага 12
        14. Нажать на кнопку "Save"
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.admin_page.click_admin_link()
