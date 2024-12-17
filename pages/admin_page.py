import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    PAGE_URL = Links.ADMIN_PAGE

    LINK_ADMIN = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[1]")

    @allure.step("Click on 'Admin' link")
    def click_admin_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_ADMIN)
        ).click()
