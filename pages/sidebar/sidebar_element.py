import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SidebarElements(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    """Элементы навигационной панели"""
    SWITCH_BUTTON = ("xpath", "//button[@role = 'none']")

    LINK_BUZZ = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[12]")
    LINK_CLAIM = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[11]")

    LINK_MAINTENANCE = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[10]")
    PASSWORD_FIELD_MAINTENANCE = ("xpath", "//input[@type = 'password']")
    CONFIRM_BUTTON_MAINTENANCE = ("xpath", "//button[@type = 'submit']")

    LINK_DIRECTORY = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[9]")
    LINK_DASHBOARD = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[8]")
    LINK_PERFORMANCE = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[7]")
    LINK_MY_INFO = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[6]")
    LINK_RECRUITMENT = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[5]")
    LINK_TIME = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[4]")
    LINK_LEAVE = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[3]")
    LINK_PIM = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[2]")
    LINK_ADMIN = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[1]")

    SEARCH_FIELD = ("xpath", "//input[@placeholder='Search']")
    LINK_TIME_AFTER_SEARCH = ("xpath", "//span[text()='Time']")

    def click_switch_button(self):
        with allure.step("Click on 'Switch' button"):
            self.wait.until(
                EC.element_to_be_clickable(self.SWITCH_BUTTON)
            ).click()
            time.sleep(1)

    def click_buzz_link(self):
        with allure.step("Click on 'Buzz' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_BUZZ)
            ).click()
            assert Links.BUZZ_PAGE == self.driver.current_url

    def click_claim_link(self):
        with allure.step("Click on 'Claim' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_CLAIM)
            ).click()
            assert Links.CLAIM_PAGE == self.driver.current_url

    def click_maintenance_link(self, password):
        with allure.step("Click on 'Maintenance' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_MAINTENANCE)
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(self.PASSWORD_FIELD_MAINTENANCE)
            ).send_keys(password)
            self.wait.until(  # переписать в будущем отдельной функцией !!!
                EC.element_to_be_clickable(self.CONFIRM_BUTTON_MAINTENANCE)
            ).click()
            assert Links.MAINTENANCE_PAGE == self.driver.current_url

    def click_directory_link(self):
        with allure.step("Click on 'Directory' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_DIRECTORY)
            ).click()
            assert Links.DIRECTORY_PAGE == self.driver.current_url

    def click_dashboard_link(self):
        with allure.step("Click on 'Dashboard' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_DASHBOARD)
            ).click()
            assert Links.DASHBOARD_PAGE == self.driver.current_url

    def click_performance_link(self):
        with allure.step("Click on 'Performance' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_PERFORMANCE)
            ).click()
            assert Links.PERFORMANCE_PAGE == self.driver.current_url

    def click_my_info_link(self):
        with allure.step("Click on 'My Info' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_MY_INFO)
            ).click()
            assert Links.MY_INFO_PAGE == self.driver.current_url

    def click_recruitment_link(self):
        with allure.step("Click on 'Recruitment' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_RECRUITMENT)
            ).click()
            assert Links.RECRUITMENT_PAGE == self.driver.current_url

    def click_time_link(self):
        with allure.step("Click on 'Time' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_TIME)
            ).click()
            assert Links.TIME_PAGE == self.driver.current_url

    def click_leave_link(self):
        with allure.step("Click on 'Leave' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_LEAVE)
            ).click()
            assert Links.LEAVE_PAGE == self.driver.current_url

    def click_pim_link(self):
        with allure.step("Click on 'PIM' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_PIM)
            ).click()
            assert Links.PIM_PAGE == self.driver.current_url

    def click_admin_link(self):
        with allure.step("Click on 'Admin' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_ADMIN)
            ).click()
            assert Links.ADMIN_PAGE == self.driver.current_url

    def enter_search_query(self, query):
        with allure.step("Enter search query /Time/"):
            self.wait.until(
                EC.element_to_be_clickable(self.SEARCH_FIELD)
            ).send_keys(query)
            value_search = self.wait.until(
                EC.element_to_be_clickable(self.SEARCH_FIELD)
            ).get_attribute("value")
            assert value_search == query
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_TIME_AFTER_SEARCH)
            ).click()




