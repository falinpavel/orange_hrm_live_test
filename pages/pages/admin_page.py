import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    PAGE_URL = Links.ADMIN_PAGE

    LINK_ADMIN = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[1]")
    USERNAME_TEXT = ("xpath", "//label[normalize-space()='Username']")
    USERNAME_FIELD = ("xpath", "(//div/input[@class='oxd-input oxd-input--active'])[2]")
    USER_ROLE_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
    USER_ROLE_TEXT = ("xpath", "//label[normalize-space()='User Role']")
    USER_ROLE_ADMIN = ("xpath", "//div[@role='option']/span[text()='Admin']")

    @allure.step("Click on 'Admin' link")
    def click_admin_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_ADMIN)
        ).click()
