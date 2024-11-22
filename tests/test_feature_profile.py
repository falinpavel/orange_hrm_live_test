"""Тестирование страницы профиля сотрудника."""
import random
import allure
# import pytest
from base.base_test import BaseTest


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
        # self.profile_page.change_employee_info(
        #     f"Test{random.randint(1, 100)}",
        #     f"Test{random.randint(1, 100)}",
        #     f"Test{random.randint(1, 100)}"
        # )
        self.profile_page.change_first_name(f"Test {random.randint(1, 100)}")
        self.profile_page.change_middle_name(f"Test {random.randint(1, 100)}")
        self.profile_page.change_second_name(f"Test {random.randint(1, 100)}")
        self.profile_page.click_save_changes()
        # self.profile_page.is_changes_saved()
        self.profile_page.make_screenshot("test_change_employee_info")