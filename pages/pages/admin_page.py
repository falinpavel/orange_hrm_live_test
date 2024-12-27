import time
import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    PAGE_URL = Links.ADMIN_PAGE

    # for page add (postfix ADD)
    LINK_ADMIN = ("xpath", "(//ul[@class= 'oxd-main-menu']/li)[1]")
    USER_BUTTON_ADD = ("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    USERNAME_TEXT_ADD = ("xpath", "//label[normalize-space()='Username']")
    EMPLOYEE_NAME_FIELD_ADD = ("xpath", "(//input)[2]")
    USERNAME_FIELD_ADD = ("xpath", "(//input)[3]")
    PASSWORD_TEXT_ADD = ("xpath", "//label[normalize-space()='Password']")
    PASSWORD_FIELD_ADD = ("xpath", "(//input)[4]")
    CONFIRM_PASSWORD_TEXT_ADD = ("xpath", "//label[normalize-space()='Confirm Password']")
    CONFIRM_PASSWORD_FIELD_ADD = ("xpath", "(//input)[5]")
    HINT_TEXT_ADD = ("xpath", "//p[@class='oxd-text oxd-text--p user-password-hint']") # For a strong password, please use a hard to guess combination of text with upper and lower case characters, symbols and numbers
    HINT_REQ_USER_ROLE_ADD = ("xpath", "(//span[text()='Required'])[1]")
    HINT_REQ_EMPLOYEE_NAME_ADD = ("xpath", "(//span[text()='Required'])[2]")
    HINT_REQ_STATUS_ADD = ("xpath", "(//span[text()='Required'])[3]")
    HINT_REQ_USERNAME_ADD = ("xpath", "(//span[text()='Required'])[4]")
    HINT_REQ_PASSWORD_ADD = ("xpath", "(//span[text()='Required'])[5]")
    HINT_REQ_CONFIRM_PASSWORD_ADD = ("xpath", "//span[text()='Passwords do not match']")
    BUTTON_CANCEL_ADD = ("xpath", "(//button)[4]")
    BUTTON_SAVE_ADD = ("xpath", "(//button)[5]")
    # for page search
    USERNAME_TEXT_SEARCH = ("xpath", "//label[normalize-space()='Username']")
    USERNAME_FIELD_SEARCH = ("xpath", "(//input)[2]")
    USER_ROLE_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
    USER_ROLE_TEXT = ("xpath", "//label[normalize-space()='User Role']")
    USER_ROLE_ADMIN = ("xpath", "//div[@role='option']/span[text()='Admin']")
    USER_ROLE_ESS = ("xpath", "//div[@role='option']/span[text()='ESS']")
    EMPLOYEE_NAME_TEXT = ("xpath", "//label[normalize-space()='Employee Name']")
    EMPLOYEE_NAME_FIELD_SEARCH = ("xpath", "(//input)[3]")
    STATUS_TEXT = ("xpath", "//label[normalize-space()='Status']")
    STATUS_DROPDOWN = ("xpath", "//div[@class='oxd-select-text oxd-select-text--focus']")
    STATUS_DROPDOWN_ENABLED = ("xpath", "//div[@role='option']/span[text()='Enabled']")
    STATUS_DROPDOWN_DISABLED = ("xpath", "//div[@role='option']/span[text()='Disabled']")

    def click_admin_link(self):
        with allure.step("Click on 'Admin' link"):
            self.wait.until(
                EC.element_to_be_clickable(self.LINK_ADMIN)
            ).click()

    def click_add_button(self):
        with allure.step("Click on 'Add' button"):
            self.wait.until(
                EC.element_to_be_clickable(self.USER_BUTTON_ADD)
            ).click()
            time.sleep(1)
            assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser" # TODO fix

    def add_username_field(self, username): # TODO back to work later
        with allure.step("Enter username"):
            name_field = self.wait.until(
                EC.element_to_be_clickable(self.USERNAME_TEXT_SEARCH)
            ).text
            assert name_field == 'Username'
            new_value = self.wait.until(
                EC.element_to_be_clickable(self.USERNAME_FIELD_SEARCH)
            )
            new_value.click()
            new_value.send_keys(Keys.CONTROL + "a")
            new_value.send_keys(Keys.DELETE)
            new_value.send_keys(username)
            assert new_value.get_attribute("value") == username

    def add_user_role_dropdown(self, user_role): # TODO back to work later
        with allure.step("Click on 'User Role' dropdown"):
            name_field = self.wait.until(
                EC.element_to_be_clickable(self.USER_ROLE_TEXT)
            ).text
            assert name_field == 'User Role'
            self.wait.until(
                EC.element_to_be_clickable(self.USER_ROLE_DROPDOWN)
            ).click()
            if user_role == 'Admin':
                self.wait.until(
                    EC.element_to_be_clickable(self.USER_ROLE_ADMIN)
                ).click()
                value = self.wait.until(
                    EC.element_to_be_clickable(self.USER_ROLE_DROPDOWN)
                ).text
                assert value == 'Admin'
            elif user_role == 'ESS':
                self.wait.until(
                    EC.element_to_be_clickable(self.USER_ROLE_ESS)
                ).click()
                value = self.wait.until(
                    EC.element_to_be_clickable(self.USER_ROLE_DROPDOWN)
                ).text
                assert value == 'ESS'
            else:
                raise Exception("Can't click on 'User Role' dropdown")

    def add_employee_name_field(self, employee_name): # TODO back to work later
        with allure.step("Enter employee name"):
            name_field = self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_NAME_TEXT)
            ).text
            assert name_field == 'Employee Name'
            new_value = self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_NAME_FIELD_SEARCH)
            )
            new_value.click()
            new_value.send_keys(Keys.CONTROL + "a")
            new_value.send_keys(Keys.DELETE)
            new_value.send_keys(employee_name)
            assert new_value.get_attribute("value") == employee_name

    def add_status_dropdown(self, status): # TODO back to work later
        with allure.step("Click on 'Status' dropdown"):
            name_field = self.wait.until(
                EC.element_to_be_clickable(self.STATUS_TEXT)
            ).text
            assert name_field == 'Status'
            self.wait.until(
                EC.element_to_be_clickable(self.STATUS_DROPDOWN)
            ).click()
            if status == 'Enabled':
                self.wait.until(
                    EC.element_to_be_clickable(self.STATUS_DROPDOWN_ENABLED)
                ).click()
                value = self.wait.until(
                    EC.element_to_be_clickable(self.STATUS_DROPDOWN)
                ).text
                assert value == 'Enabled'
            elif status == 'Disabled':
                self.wait.until(
                    EC.element_to_be_clickable(self.STATUS_DROPDOWN_DISABLED)
                ).click()
                value = self.wait.until(
                    EC.element_to_be_clickable(self.STATUS_DROPDOWN)
                ).text
                assert value == 'Disabled'
            else:
                raise Exception("Can't click on 'Status' dropdown")

