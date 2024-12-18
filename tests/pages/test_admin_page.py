import random
import allure
from base.base_test import BaseTest


@allure.feature("Admin page")
class TestAdminPage(BaseTest):
    @allure.title("Check admin page")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_admin_page(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
