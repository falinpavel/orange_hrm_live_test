import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SidebarElements(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE  # this is main page?

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

    @allure.step("Click on 'Switch' button")
    def click_switch_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SWITCH_BUTTON)
        ).click()

    @allure.step("Click on 'Buzz' link")
    def click_buzz_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_BUZZ)
        ).click()

    @allure.step("Click on 'Claim' link")
    def click_claim_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_CLAIM)
        ).click()

    @allure.step("Click on 'Maintenance' link")
    def click_maintenance_link(self, password):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_MAINTENANCE)
        ).click()
        self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_FIELD_MAINTENANCE)
        ).send_keys(password)
        self.wait.until(  # переписать в будущем отдельной функцией !!!
            EC.element_to_be_clickable(self.CONFIRM_BUTTON_MAINTENANCE)
        ).click()

    @allure.step("Click on 'Directory' link")
    def click_directory_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_DIRECTORY)
        ).click()

    @allure.step("Click on 'Dashboard' link")
    def click_dashboard_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_DASHBOARD)
        ).click()

    @allure.step("Click on 'Performance' link")
    def click_performance_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_PERFORMANCE)
        ).click()

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_MY_INFO)
        ).click()

    @allure.step("Click on 'Recruitment' link")
    def click_recruitment_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_RECRUITMENT)
        ).click()

    @allure.step("Click on 'Time' link")
    def click_time_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_TIME)
        ).click()

    @allure.step("Click on 'Leave' link")
    def click_leave_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_LEAVE)
        ).click()

    @allure.step("Click on 'PIM' link")
    def click_pim_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_PIM)
        ).click()

    @allure.step("Click on 'Admin' link")
    def click_admin_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_ADMIN)
        ).click()

    @allure.step("Enter search query")
    def enter_search_query(self, query):
        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_FIELD)
        ).send_keys(query)
        """Дописать тесты для поиска"""
