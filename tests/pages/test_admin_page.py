import allure
import pytest
from base.base_test import BaseTest
import utils.faker_data as FD


@allure.feature("Admin page tests")
class TestAdminPage(BaseTest):

    @allure.title("Add user admin")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_new_user_admin(self):
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
        11. Нажать на кнопку "Save"
        12. Проверить, что открылась страница администратора
        13. Нажать на ссылку "Admin"
        14. Проверить, что открылась страница администратора
        15. Нажать на ссылку "Logout"
        16. Проверить, что открылась главная страница
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.admin_page.click_admin_link()
        self.admin_page.click_add_button()
        self.admin_page.add_user_role_dropdown("Admin")

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
        self.admin_page.add_username_field(FD.fake_admin()[0])
        self.admin_page.add_user_role_dropdown("Admin")
        # self.admin_page.add_employee_name_field(FD.fake_admin()[2])
        self.admin_page.add_status_dropdown("Enabled")

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
