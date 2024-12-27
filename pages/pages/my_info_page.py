import time
import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class ProfilePage(BasePage):
    PAGE_URL = Links.MY_INFO_PAGE
    EMPLOYEE_FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    EMPLOYEE_MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    EMPLOYEE_SECOND_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    EMPLOYEE_NICKNAME_FIELD = ("xpath", "(//div/input)[5]")
    EMPLOYEE_ID_FIELD = ("xpath", "(//div/input)[6]")
    EMPLOYEE_OTHER_ID_FIELD = ("xpath", "(//div/input)[7]")
    EMPLOYEE_DLN_FIELD = ("xpath", "(//div/input)[8]")
    EMPLOYEE_LXD_DATE_FIELD = ("xpath", "(//div/input)[9]")
    EMPLOYEE_LXD_DATE_ALERT = (
        "xpath", "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
    EMPLOYEE_NATIONALITY_DROPDOWN = ("xpath", "(//div[@class='oxd-select-wrapper'])[1]")
    EMPLOYEE_NATIONALITY_DROPDOWN_SELECT = ("xpath", "//div[@role='option']/span[text()='Russian']")
    EMPLOYEE_MARITAL_STATUS_DROPDOWN = ("xpath", "(//div[@class='oxd-select-wrapper'])[2]")
    EMPLOYEE_MARITAL_VALUE_FIELD = ("xpath", "(//div[@class='oxd-select-text-input'])[2]")
    EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_MARIED = ("xpath", "//div[@role='option']/span[text()='Married']")
    EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_SINGLE = ("xpath", "//div[@role='option']/span[text()='Single']")
    EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_OTHER = ("xpath", "//div[@role='option']/span[text()='Other']")

    EMPLOYEE_BIRTH_DATE_FIELD = ("xpath", "//div/input)[9]")

    EMPLOYEE_GENDER_MALE = ("xpath", "//input[@value='1']")
    EMPLOYEE_GENDER_FEMALE = ("xpath", "//input[@value='2']")

    SAVE_BUTTON_PERSONAL = ("xpath", "(//button[@type = 'submit'])[1]")
    EMPLOYEE_BLOOD_TYPE_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
    EMPLOYEE_TEST_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[7]")
    SAVE_BUTTON_CUSTOM = ("xpath", "(//button[@type = 'submit'])[2]")
    EMPLOYEE_ADD_ATTACHMENT_BUTTON = ("xpath", "//button[normalize-space()='Add']")

    def change_first_name(self, new_first_name):
        with allure.step(f"Change first name on {new_first_name}"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_FIRST_NAME_FIELD)
            )
            time.sleep(1)
            first_name_field.click()
            first_name_field.send_keys(Keys.CONTROL + "a")
            first_name_field.send_keys(Keys.DELETE)
            self.wait.until(
                lambda driver: first_name_field.get_attribute("value") == "",
                "First name is not empty"
            )
            first_name_field.send_keys(new_first_name)
            assert first_name_field.get_attribute("value") == new_first_name, \
                f"Expected: {new_first_name}, Actual: {first_name_field.get_attribute('value')}"

    def change_middle_name(self, new_middle_name):
        with allure.step(f"Change middle name on {new_middle_name}"):
            middle_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_MIDDLE_NAME_FIELD)
            )
            time.sleep(1)
            middle_name.click()
            middle_name.send_keys(Keys.CONTROL + "a")
            middle_name.send_keys(Keys.DELETE)
            self.wait.until(
                lambda driver: middle_name.get_attribute("value") == "",
                "Middle name is not empty"
            )
            middle_name.send_keys(new_middle_name)
            assert middle_name.get_attribute("value") == new_middle_name, \
                f"Expected: {new_middle_name}, Actual: {middle_name.get_attribute('value')}"

    def change_second_name(self, new_second_name):
        with allure.step(f"Change second name on {new_second_name}"):
            second_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_SECOND_NAME_FIELD)
            )
            time.sleep(1)
            second_name.click()
            second_name.send_keys(Keys.CONTROL + "a")
            second_name.send_keys(Keys.DELETE)
            self.wait.until(
                lambda driver: second_name.get_attribute("value") == "",
                "Second name is not empty"
            )
            second_name.send_keys(new_second_name)
            assert second_name.get_attribute("value") == new_second_name, \
                f"Expected: {new_second_name}, Actual: {second_name.get_attribute('value')}"

    def change_nickname(self, new_nickname):
        with allure.step(f"Change nickname on {new_nickname}"):
            nickname = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_NICKNAME_FIELD)
            )
            time.sleep(1)
            nickname.click()
            nickname.send_keys(Keys.CONTROL + "a")
            nickname.send_keys(Keys.DELETE)
            self.wait.until(
                lambda driver: nickname.get_attribute("value") == "",
                "Nickname is not empty"
            )
            nickname.send_keys(new_nickname)
            assert nickname.get_attribute("value") == new_nickname, \
                f"Expected: {new_nickname}, Actual: {nickname.get_attribute('value')}"

    def change_employee_id(self, new_id):
        with allure.step(f"Change employee id on {new_id}"):
            employee_id = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_ID_FIELD)
            )
            time.sleep(1)
            employee_id.click()
            employee_id.send_keys(Keys.CONTROL + "a")
            employee_id.send_keys(Keys.DELETE)
            self.wait.until(
                lambda driver: employee_id.get_attribute("value") == "",
                "Employee id is not empty"
            )
            employee_id.send_keys(new_id)
            assert employee_id.get_attribute("value") == new_id, \
                f"Expected: {new_id}, Actual: {employee_id.get_attribute('value')}"

    def change_other_id(self, new_other_id):
        with allure.step(f"Change other id on {new_other_id}"):
            other_id = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_OTHER_ID_FIELD)
            )
            time.sleep(1)
            other_id.click()
            other_id.send_keys(Keys.CONTROL + "a")
            other_id.send_keys(Keys.DELETE)
            self.wait.until(
                lambda driver: other_id.text == "",
                "Other id is not empty"
            )
            other_id.send_keys(new_other_id)
            assert other_id.get_attribute("value") == new_other_id

    def change_dln(self, new_dln):
        with allure.step(f"Change dln on {new_dln}"):
            dln = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_DLN_FIELD)
            )
            time.sleep(1)
            dln.click()
            dln.send_keys(Keys.CONTROL + "a")
            dln.send_keys(Keys.DELETE)
            assert dln.get_attribute("value") == "", \
                f"Expected: , Actual: {dln.get_attribute('value')}"
            dln.send_keys(new_dln)
            assert dln.get_attribute("value") == new_dln, \
                f"Expected: {new_dln}, Actual: {dln.get_attribute('value')}"

    def change_lxd_date(self, new_lxd_date, other_format):
        with allure.step(f"Change lxd date on {new_lxd_date}"):
            lxd_date_field = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_LXD_DATE_FIELD)
            )
            time.sleep(1)
            lxd_date_field.click()
            lxd_date_field.send_keys(Keys.CONTROL + "a")
            lxd_date_field.send_keys(Keys.DELETE)
            lxd_date_field.send_keys(new_lxd_date)
            self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_NATIONALITY_DROPDOWN)
            ).click()
            time.sleep(1)
            message_alert = self.wait.until(EC.presence_of_element_located(
                self.EMPLOYEE_LXD_DATE_ALERT)
            ).get_attribute("value")
            if message_alert == "Should be a valid date in yyyy-mm-dd format":
                other_date = self.wait.until(EC.element_to_be_clickable(
                    self.EMPLOYEE_LXD_DATE_FIELD
                ))
                other_date.click()
                other_date.send_keys(Keys.CONTROL + "a")
                other_date.send_keys(Keys.DELETE)
                other_date.send_keys(other_format)
            else:
                Exception(message_alert)
            assert lxd_date_field.get_attribute("value") == new_lxd_date, \
                f"Expected: {new_lxd_date}, Actual: {lxd_date_field.get_attribute('value')}"

    def change_nationality(self):  # TODO: need to be fixed, add exeptions
        with allure.step("Change nationality on Russian"):
            self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_NATIONALITY_DROPDOWN)
            ).click()
            time.sleep(1)
            self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_NATIONALITY_DROPDOWN_SELECT)
            ).click()
            time.sleep(1)
            old_value = self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_NATIONALITY_DROPDOWN)
            ).text
            new_value = self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_NATIONALITY_DROPDOWN)
            ).text
            assert new_value == old_value

    def change_marital_status(self):
        with allure.step("Change marital status"):
            before_marital_status = self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_VALUE_FIELD)
            ).text
            self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN)
            ).click()
            time.sleep(1)
            if before_marital_status == "-- Select --":
                value = self.wait.until(
                    EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_SINGLE)
                ).text
                assert value == "Single"
                self.wait.until(
                    EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_SINGLE)
                ).click()
                time.sleep(1)
            elif before_marital_status == "Married":
                value = self.wait.until(
                    EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_SINGLE)
                ).text
                assert value == "Single"
                self.wait.until(
                    EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_SINGLE)
                ).click()
                time.sleep(1)
            elif before_marital_status == "Single":
                value = self.wait.until(
                    EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_MARIED)
                ).text
                assert value == "Married"
                self.wait.until(
                    EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_MARIED)
                ).click()
                time.sleep(1)
            elif before_marital_status == "Other":
                value = self.wait.until(
                    EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_MARIED)
                ).text
                assert value == "Married"
                self.wait.until(
                    EC.element_to_be_clickable(self.EMPLOYEE_MARITAL_STATUS_DROPDOWN_SELECT_MARIED)
                ).click()
                time.sleep(1)
            else:
                assert False, "Expected: 'Married', 'Single' or 'Other'"

    def change_birth_date(self, new_birth_date):
        with allure.step(f"Change birth date on {new_birth_date}"):
            birth_date = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_BIRTH_DATE_FIELD)
            )
            time.sleep(1)
            birth_date.click()
            birth_date.send_keys(Keys.CONTROL + "a")
            birth_date.send_keys(Keys.DELETE)
            birth_date.send_keys(new_birth_date)
            assert birth_date.get_attribute("value") == new_birth_date, \
                f"Expected: {new_birth_date}, Actual: {birth_date.get_attribute('value')}"

    def change_gender_radio_button(self):
        with allure.step("Change gender radio button"):
            male_radio = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_GENDER_MALE)
            )
            female_radio = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_GENDER_FEMALE)
            )
            male_radio.click()
            female_radio.click()

    def click_save_changes(self):
        with allure.step("Click on 'Save' button"):
            self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_PERSONAL)).click()
