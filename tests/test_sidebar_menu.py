import allure
from base.base_test import BaseTest

"""
Тест кейс: Проверка меню сайдбара. 

Gherkin:
    Scenario: Проверка меню сайдбара
        Given Я вошел в систему
        And Переход на страницу "Buzz"
        And Переход на страницу "Claim"
        And Переход на страницу "Maintenance" по паролю
        And Переход на страницу "Directory"
        And Переход на страницу "Dashboard"
        And Переход на страницу "Performance"
        And Переход на страницу "My Info"
        And Переход на страницу "Recruitment"
        And Переход на страницу "Time"
        And Переход на страницу "Leave"
        And Переход на страницу "PIM"
        And Переход на страницу "Admin"
        And Клик по кнопке "Switch"
        Then Меню сайдбара проверено
"""

@allure.feature("Sidebar menu")
class TestSidebarMenu(BaseTest):
    @allure.title("Check sidebar menu")
    @allure.severity("Normal")
    # @pytest.mark.smoke
    def test_check_sidebar_menu(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        """Прыгаем по страницам сайдбара"""
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
        self.sidebar_element.click_switch_button() # double click


        # self.make_screenshot("test_check_sidebar_menu")
