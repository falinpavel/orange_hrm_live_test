import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE
    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")
    MES_INFOS_BUTTON = ("xpath", "//span[text()='Mes Infos']")

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        with allure.step("Click on 'My Info' link"):
            value = self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).text
            self.wait.until(
                EC.element_to_be_clickable(self.MY_INFO_BUTTON)
            ).click()
            assert Links.MY_INFO_PAGE == self.driver.current_url
            if value is None:
                self.wait.until(
                    EC.element_to_be_clickable(self.MES_INFOS_BUTTON)
                ).click()
                assert Links.MY_INFO_PAGE == self.driver.current_url
