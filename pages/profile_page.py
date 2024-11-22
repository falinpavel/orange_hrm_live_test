import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    PAGE_URL = Links.PERSONAL_DETAILS_PAGE
    EMPLOYEE_FIRST_NAME_FIELD = (
        "xpath", "//input[@name = 'firstName']"
    )
    EMPLOYEE_MIDDLE_NAME_FIELD = (
        "xpath", "//input[@name = 'middleName']"
    )
    EMPLOYEE_SECOND_NAME_FIELD = (
        "xpath", "//input[@name = 'lastName']"
    )
    SAVE_BUTTON = (
        "xpath", "(//button[@type = 'submit'])[1]"
    )

    # def change_employee_info(self, new_first_name, new_middle_name, new_second_name):
    #     with allure.step(
    #             f"Change first name on {new_first_name}, middle name on {new_middle_name}, second name on {new_second_name}"
    #     ):
    #         """Изменение имя сотрудника"""
    #         first_name_field = self.wait.until(EC.element_to_be_clickable(
    #             self.EMPLOYEE_FIRST_NAME_FIELD)
    #         )
    #         first_name_field.click()
    #         first_name_field.clear()
    #         # assert first_name_field.get_attribute("value") == "", "First name is not empty"
    #         first_name_field.send_keys(new_first_name)
    #         self.new_value_first_name = new_first_name
    #         """Изменение отчества сотрудника"""
    #         middle_name = self.wait.until(EC.element_to_be_clickable(
    #             self.EMPLOYEE_MIDDLE_NAME_FIELD)
    #         )
    #         middle_name.click()
    #         middle_name.clear()
    #         # assert middle_name.get_attribute("value") == "", "Middle name is not empty"
    #         middle_name.send_keys(new_middle_name)
    #         self.new_value_middle_name = new_middle_name
    #         """Изменение фамилии сотрудника"""
    #         second_name = self.wait.until(EC.element_to_be_clickable(
    #             self.EMPLOYEE_SECOND_NAME_FIELD)
    #         )
    #         second_name.click()
    #         second_name.clear()
    #         # assert second_name.get_attribute("value") == "", "Second name is not empty"
    #         second_name.send_keys(new_second_name)
    #         self.new_value_second_name = new_second_name

    def change_first_name(self, new_first_name):
        with allure.step(f"Change first name on {new_first_name}"):
            """Изменение имя сотрудника"""
            first_name_field = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_FIRST_NAME_FIELD)
            )
            first_name_field.click()
            first_name_field.clear()
            # assert first_name_field.get_attribute("value") == "", "First name is not empty"
            first_name_field.send_keys(new_first_name)
            self.name = new_first_name

    def change_middle_name(self, new_middle_name):
        with allure.step(f"Change middle name on {new_middle_name}"):
            middle_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_MIDDLE_NAME_FIELD)
            )
            middle_name.click()
            middle_name.clear()
            # assert middle_name.get_attribute("value") == "", "Middle name is not empty"
            middle_name.send_keys(new_middle_name)
            self.name = new_middle_name

    def change_second_name(self, new_second_name):
        with allure.step(f"Change second name on {new_second_name}"):
            second_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_SECOND_NAME_FIELD)
            )
            second_name.click()
            second_name.clear()
            # assert second_name.get_attribute("value") == "", "Second name is not empty"
            second_name.send_keys(new_second_name)
            self.name = new_second_name

    @allure.step("Click on 'Save' button")
    def click_save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

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
