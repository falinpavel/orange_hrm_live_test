import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    PAGE_URL = Links.MY_INFO_PAGE

    """Personal Details"""
    EMPLOYEE_FIRST_NAME_FIELD = ("xpath", "//input[@name = 'firstName']")
    EMPLOYEE_MIDDLE_NAME_FIELD = ("xpath", "//input[@name = 'middleName']")
    EMPLOYEE_SECOND_NAME_FIELD = ("xpath", "//input[@name = 'lastName']")
    EMPLOYEE_ID_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    EMPLOYEE_OTHER_ID_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[3]")
    EMPLOYEE_DLN_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[4]")
    EMPLOYEE_LXD_DATE_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[5]")
    EMPLOYEE_NATIONALITY_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
    EMPLOYEE_MARITAL_STATUS_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
    EMPLOYEE_BIRTH_DATE_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[6]")
    EMPLOYEE_GENDER_NALE = ("xpath", "//input[@value='1']")
    EMPLOYEE_GENDER_FEMALE = ("xpath", "//input[@value='2']")
    SAVE_BUTTON_PERSONAL = ("xpath", "(//button[@type = 'submit'])[1]")

    """Custom Fields"""
    EMPLOYEE_BLOOD_TYPE_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
    EMPLOYEE_TEST_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[7]")
    SAVE_BUTTON_CUSTOM = ("xpath", "(//button[@type = 'submit'])[2]")
    """Atachments"""
    EMPLOYEE_ADD_ATTACHMENT_BUTTON = ("xpath", "//button[normalize-space()='Add']")

    """Personal Details"""

    def change_first_name(self, new_first_name):
        with allure.step(f"Change first name on {new_first_name}"):
            """Изменение имя сотрудника"""
            first_name_field = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_FIRST_NAME_FIELD)
            )
            first_name_field.click()
            first_name_field.send_keys(Keys.BACKSPACE * 10)  # очищаем поле
            # assert first_name_field.get_attribute("value") == "", "First name is not empty"
            first_name_field.send_keys(new_first_name)
            self.name = new_first_name

    def change_middle_name(self, new_middle_name):
        with allure.step(f"Change middle name on {new_middle_name}"):
            middle_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_MIDDLE_NAME_FIELD)
            )
            middle_name.click()
            middle_name.send_keys(Keys.BACKSPACE * 10)
            # assert middle_name.get_attribute("value") == "", "Middle name is not empty"
            middle_name.send_keys(new_middle_name)
            self.name = new_middle_name

    def change_second_name(self, new_second_name):
        with allure.step(f"Change second name on {new_second_name}"):
            second_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_SECOND_NAME_FIELD)
            )
            second_name.click()
            second_name.send_keys(Keys.BACKSPACE * 10)
            # assert second_name.get_attribute("value") == "", "Second name is not empty"
            second_name.send_keys(new_second_name)
            self.name = new_second_name

    def change_employee_id(self, new_id):
        with allure.step(f"Change employee id on {new_id}"):
            employee_id = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_ID_FIELD)
            )
            employee_id.click()
            employee_id.send_keys(Keys.BACKSPACE * 10)
            # assert employee_id.get_attribute("value") == "", "Employee id is not empty"
            employee_id.send_keys(new_id)
            self.id = new_id

    def change_other_id(self, new_other_id):
        with allure.step(f"Change other id on {new_other_id}"):
            other_id = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_OTHER_ID_FIELD)
            )
            other_id.click()
            other_id.send_keys(Keys.BACKSPACE * 10)
            # assert other_id.get_attribute("value") == "", "Other id is not empty"
            other_id.send_keys(new_other_id)
            self.other_id = new_other_id

    def change_dln(self, new_dln):
        with allure.step(f"Change dln on {new_dln}"):
            dln = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_DLN_FIELD)
            )
            dln.click()
            dln.send_keys(Keys.BACKSPACE * 10)
            # assert dln.get_attribute("value") == "", "Dln is not empty"
            dln.send_keys(new_dln)
            self.dln = new_dln

    def change_lxd_date(self, new_lxd_date):
        with allure.step(f"Change lxd date on {new_lxd_date}"):
            lxd_date = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_LXD_DATE_FIELD)
            )
            lxd_date.click()
            lxd_date.send_keys(Keys.BACKSPACE * 10)
            # assert lxd_date.get_attribute("value") == "", "Lxd date is not empty"
            lxd_date.send_keys(new_lxd_date)
            self.lxd_date = new_lxd_date

    def change_nationality(self, new_nationality):
        with allure.step(f"Change nationality on {new_nationality}"):
            nationality = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_NATIONALITY_DROPDOWN)
            )
            nationality.click()
            nationality.send_keys(Keys.BACKSPACE * 10)
            # assert nationality.get_attribute("value") == "", "Nationality is not empty"
            nationality.send_keys(new_nationality)
            self.nationality = new_nationality

    def change_marital_status(self, new_marital_status):
        with allure.step(f"Change marital status on {new_marital_status}"):
            marital_status = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_MARITAL_STATUS_DROPDOWN)
            )
            marital_status.click()
            marital_status.send_keys(Keys.BACKSPACE * 10)
            # assert marital_status.get_attribute("value") == "", "Marital status is not empty"
            marital_status.send_keys(new_marital_status)
            self.marital_status = new_marital_status

    def change_birth_date(self, new_birth_date):
        with allure.step(f"Change birth date on {new_birth_date}"):
            birth_date = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_BIRTH_DATE_FIELD)
            )
            birth_date.click()
            birth_date.send_keys(Keys.BACKSPACE * 10)
            # assert birth_date.get_attribute("value") == "", "Birth date is not empty"
            birth_date.send_keys(new_birth_date)
            self.birth_date = new_birth_date

    # def change_gender(self, new_gender):
    #     with allure.step(f"Change gender on {new_gender}"):

    @allure.step("Click on 'Save' button")
    def click_save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_PERSONAL)).click()

    # @allure.step("Check that changes are saved")
    # def is_changes_saved(self):
    #     self.wait.until(EC.text_to_be_present_in_element_value(
    #         self.EMPLOYEE_FIRST_NAME_FIELD, self.new_value_first_name)
    #     )
    #     self.wait.until(EC.text_to_be_present_in_element_value(
    #         self.EMPLOYEE_MIDDLE_NAME_FIELD, self.new_value_middle_name)
    #     )
    #     self.wait.until(EC.text_to_be_present_in_element_value(
    #         self.EMPLOYEE_SECOND_NAME_FIELD, self.new_value_second_name)
    #     )
