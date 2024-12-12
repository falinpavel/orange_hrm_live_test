import random
import allure
from base.base_test import BaseTest

"""
Тест кейс: Изменение информации о сотруднике. 

Gherkin:
    Scenario: Изменение информации о сотруднике
        Given Я вошел в систему
        And Переход на страницу "My Info"
        When Изменить имя сотрудника
        And Изменить отчество сотрудника
        And Изменить фамилию сотрудника
        And Изменить ID сотрудника
        And Изменить другой ID сотрудника
        And Изменить DLN сотрудника
        And Изменить LXD date сотрудника
        And Сохранить изменения
        Then Изменения сохранены
"""


@allure.feature("Profile change")
class TestProfileFeatureTest(BaseTest):
    @allure.title("Change employee info")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_change_employee_info(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.click_my_info_link()
        self.profile_page.change_first_name(f"Test {random.randint(1, 100)}")
        self.profile_page.change_middle_name(f"Test {random.randint(1, 100)}")
        self.profile_page.change_second_name(f"Test {random.randint(1, 100)}")
        self.profile_page.change_employee_id(f"Test {random.randint(1, 100)}")
        self.profile_page.change_other_id(f"Test {random.randint(1, 100)}")
        self.profile_page.change_dln(f"Test {random.randint(1, 100)}")
        self.profile_page.change_lxd_date("2013-01-01")
        self.profile_page.click_save_changes()
        # self.profile_page.is_changes_saved()
        self.profile_page.make_screenshot("test_change_employee_info")
