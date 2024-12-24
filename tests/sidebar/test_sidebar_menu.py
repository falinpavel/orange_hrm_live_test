import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sidebar menu")
class TestSidebarMenu(BaseTest):
    @allure.title("Check sidebar menu")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_check_sidebar_menu(self):
        """
        Тест-кейс: Проверка меню бокового меню
        1. Открыть главную страницу
        2. Ввести логин
        3. Ввести пароль
        4. Нажать кнопку "Вход"
        5. Нажать на ссылку "Buzz"
        6. Нажать на ссылку "Claim"
        7. Нажать на ссылку "Maintenance"
        8. На странице "Maintenance" ввести пароль
        9. Нажать на ссылку "Directory"
        10. Нажать на ссылку "Dashboard"
        11. Нажать на ссылку "Performance"
        12. Нажать на ссылку "My Info"
        13. Нажать на ссылку "Recruitment"
        14. Нажать на ссылку "Time"
        15. Нажать на ссылку "Leave"
        16. Нажать на ссылку "PIM"
        17. Нажать на ссылку "Admin"
        18. Нажать на кнопку "Switch" для скрытия бокового меню
        19. Нажать на кнопку "Switch" для показа бокового меню
        20. Ввести поисковый запрос "Time" в поле ввода поиска
        21. Проверить, что появился результат поиска
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.sidebar_element.click_buzz_link()
        self.sidebar_element.click_claim_link()
        self.sidebar_element.click_maintenance_link(self.data.PASSWORD)
        self.sidebar_element.click_directory_link()
        self.sidebar_element.click_dashboard_link()
        self.sidebar_element.click_performance_link()
        self.sidebar_element.click_my_info_link()
        self.sidebar_element.click_recruitment_link()
        self.sidebar_element.click_time_link()
        self.sidebar_element.click_leave_link()
        self.sidebar_element.click_pim_link()
        self.sidebar_element.click_admin_link()
        self.sidebar_element.click_switch_button()
        self.sidebar_element.click_switch_button()
        self.sidebar_element.enter_search_query("Time")
