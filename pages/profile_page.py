import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    PAGE_URL = Links.MY_INFO_PAGE

    EMPLOYEE_FIRST_NAME_FIELD = ("xpath", "//input[@name = 'firstName']")
    EMPLOYEE_MIDDLE_NAME_FIELD = ("xpath", "//input[@name = 'middleName']")
    EMPLOYEE_SECOND_NAME_FIELD = ("xpath", "//input[@name = 'lastName']")
    EMPLOYEE_ID_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    EMPLOYEE_OTHER_ID_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[3]")
    EMPLOYEE_DLN_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[4]")
    EMPLOYEE_LXD_DATE_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[5]")

    EMPLOYEE_NATIONALITY_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
    EMPLOYEE_NATIONALITY_DROPDOWN_LIST = ("xpath", "//div[@role='listbox']")
    NEW_EMPLOYEE_NATIONALITY = ("xpath", "//div[@role='option']/span[text()='Angolan']")
    # NEW_EMPLOYEE_NATIONALITY = (By.XPATH, f"//div[@role='option']/span[text()='{new_nationality}']")

    EMPLOYEE_MARITAL_STATUS_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
    EMPLOYEE_BIRTH_DATE_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[6]")
    EMPLOYEE_GENDER_MALE = ("xpath", "//input[@value='1']")
    EMPLOYEE_GENDER_FEMALE = ("xpath", "//input[@value='2']")
    SAVE_BUTTON_PERSONAL = ("xpath", "(//button[@type = 'submit'])[1]")

    """Custom Fields"""
    EMPLOYEE_BLOOD_TYPE_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
    EMPLOYEE_TEST_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[7]")
    SAVE_BUTTON_CUSTOM = ("xpath", "(//button[@type = 'submit'])[2]")
    """Attachments"""
    EMPLOYEE_ADD_ATTACHMENT_BUTTON = ("xpath", "//button[normalize-space()='Add']")

    def change_first_name(self, new_first_name):
        with allure.step(f"Change first name on {new_first_name}"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_FIRST_NAME_FIELD)
            )
            first_name_field.click()
            first_name_field.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.wait.until(
                lambda driver: first_name_field.get_attribute("value") == "",
                "First name is not empty"
            )
            first_name_field.send_keys(new_first_name)
            assert first_name_field.get_attribute("value") == new_first_name, \
                f"Expected: {new_first_name}, Actual: {first_name_field.get_attribute('value')}"
            self.name = new_first_name

    def change_middle_name(self, new_middle_name):
        with allure.step(f"Change middle name on {new_middle_name}"):
            middle_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_MIDDLE_NAME_FIELD)
            )
            middle_name.click()
            middle_name.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.wait.until(
                lambda driver: middle_name.get_attribute("value") == "",
                "Middle name is not empty"
            )
            middle_name.send_keys(new_middle_name)
            assert middle_name.get_attribute("value") == new_middle_name, \
                f"Expected: {new_middle_name}, Actual: {middle_name.get_attribute('value')}"
            self.name = new_middle_name

    def change_second_name(self, new_second_name):
        with allure.step(f"Change second name on {new_second_name}"):
            second_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_SECOND_NAME_FIELD)
            )
            second_name.click()
            second_name.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.wait.until(
                lambda driver: second_name.get_attribute("value") == "",
                "Second name is not empty"
            )
            second_name.send_keys(new_second_name)
            assert second_name.get_attribute("value") == new_second_name, \
                f"Expected: {new_second_name}, Actual: {second_name.get_attribute('value')}"
            self.name = new_second_name

    def change_employee_id(self, new_id):
        with allure.step(f"Change employee id on {new_id}"):
            employee_id = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_ID_FIELD)
            )
            employee_id.click()
            employee_id.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.wait.until(
                lambda driver: employee_id.get_attribute("value") == "",
                "Employee id is not empty"
            )
            employee_id.send_keys(new_id)
            assert employee_id.get_attribute("value") == new_id, \
                f"Expected: {new_id}, Actual: {employee_id.get_attribute('value')}"
            self.id = new_id

    def change_other_id(self, new_other_id):
        with allure.step(f"Change other id on {new_other_id}"):
            other_id = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_OTHER_ID_FIELD)
            )
            other_id.click()
            other_id.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.wait.until(
                lambda driver: other_id.get_attribute("value") == "",
                "Other id is not empty"
            )
            other_id.send_keys(new_other_id)
            assert other_id.get_attribute("value") == new_other_id, \
                f"Expected: {new_other_id}, Actual: {other_id.get_attribute('value')}"
            self.other_id = new_other_id

    def change_dln(self, new_dln):
        with allure.step(f"Change dln on {new_dln}"):
            dln = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_DLN_FIELD)
            )
            dln.click()
            dln.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.wait.until(
                lambda driver: dln.get_attribute("value") == "",
                "Dln is not empty"
            )
            dln.send_keys(new_dln)
            assert dln.get_attribute("value") == new_dln, \
                f"Expected: {new_dln}, Actual: {dln.get_attribute('value')}"
            self.dln = new_dln

    def change_lxd_date(self, new_lxd_date):
        with allure.step(f"Change lxd date on {new_lxd_date}"):
            lxd_date = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_LXD_DATE_FIELD)
            )
            lxd_date.click()
            lxd_date.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            lxd_date.send_keys(new_lxd_date)
            self.lxd_date = new_lxd_date

    def change_nationality(self):
        with allure.step(f"Change nationality to"):
            nationality = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_NATIONALITY_DROPDOWN)
            )
            nationality.click()
            nationality_list = self.wait.until(EC.visibility_of_element_located(
                self.EMPLOYEE_NATIONALITY_DROPDOWN_LIST)
            )
            select_new_value = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_NATIONALITY_DROPDOWN_LIST)
            ).click()

    # def change_nationality(self, new_nationality):
    #     with allure.step(f"Change nationality on {new_nationality}"):
    #         nationality = self.wait.until(EC.element_to_be_clickable(
    #             self.EMPLOYEE_NATIONALITY_DROPDOWN)
    #         )
    #         for option in nationality.find_elements_by_tag_name("option"):
    #             if option.text == new_nationality:
    #                 option.click()
    #                 break


    def change_marital_status(self, new_marital_status):
        with allure.step(f"Change marital status on {new_marital_status}"):
            marital_status = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_MARITAL_STATUS_DROPDOWN)
            )
            marital_status.click()
            marital_status.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            marital_status.send_keys(new_marital_status)
            self.marital_status = new_marital_status

    def change_birth_date(self, new_birth_date):
        with allure.step(f"Change birth date on {new_birth_date}"):
            birth_date = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_BIRTH_DATE_FIELD)
            )
            birth_date.click()
            birth_date.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            birth_date.send_keys(new_birth_date)
            self.birth_date = new_birth_date

    @allure.step("Click on 'Save' button")
    def click_save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_PERSONAL)).click()

# import allure
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from base.base_page import BasePage
#
#
# class ProfilePage(BasePage):
#     PAGE_URL = "https://example.com/my-info"
#
#     # Локаторы вынесены в словарь для удобства
#     LOCATORS = {
#         "first_name": ("xpath", "//input[@name='firstName']"),
#         "middle_name": ("xpath", "//input[@name='middleName']"),
#         "last_name": ("xpath", "//input[@name='lastName']"),
#         "employee_id": ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]"),
#         "other_id": ("xpath", "(//input[@class='oxd-input oxd-input--active'])[3]"),
#         "dln": ("xpath", "(//input[@class='oxd-input oxd-input--active'])[4]"),
#         "lxd_date": ("xpath", "(//input[@class='oxd-input oxd-input--active'])[5]"),
#         "nationality_dropdown": ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[1]"),
#         "marital_status_dropdown": ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[2]"),
#         "birth_date": ("xpath", "(//input[@class='oxd-input oxd-input--active'])[6]"),
#         "save_button": ("xpath", "(//button[@type='submit'])[1]"),
#     }
#
#     @allure.step("Очистка и ввод текста в поле")
#     def clear_and_input_text(self, field_name: str, new_value: str):
#         """Очищает и вводит текст в указанное поле."""
#         locator = self.LOCATORS[field_name]
#         element = self.wait.until(EC.element_to_be_clickable(locator))
#         element.click()
#         element.send_keys(Keys.CONTROL + "a", Keys.DELETE)
#         self.wait.until(lambda driver: element.get_attribute("value") == "", f"{field_name} не очищено.")
#         element.send_keys(new_value)
#         assert element.get_attribute("value") == new_value, f"Ожидалось: {new_value}, Получено: {element.get_attribute('value')}"
#
#     @allure.step("Выбор значения из выпадающего списка")
#     def select_from_dropdown(self, dropdown_name: str, option_text: str):
#         """Выбор значения из выпадающего списка."""
#         dropdown_locator = self.LOCATORS[dropdown_name]
#         dropdown = self.wait.until(EC.element_to_be_clickable(dropdown_locator))
#         dropdown.click()
#         option_locator = (By.XPATH, f"//div[@role='option' and .//span[text()='{option_text}']]")
#         option = self.wait.until(EC.element_to_be_clickable(option_locator))
#         option.click()
#
#     def change_first_name(self, new_first_name: str):
#         self.clear_and_input_text("first_name", new_first_name)
#
#     def change_middle_name(self, new_middle_name: str):
#         self.clear_and_input_text("middle_name", new_middle_name)
#
#     def change_last_name(self, new_last_name: str):
#         self.clear_and_input_text("last_name", new_last_name)
#
#     def change_employee_id(self, new_id: str):
#         self.clear_and_input_text("employee_id", new_id)
#
#     def change_other_id(self, new_other_id: str):
#         self.clear_and_input_text("other_id", new_other_id)
#
#     def change_dln(self, new_dln: str):
#         self.clear_and_input_text("dln", new_dln)
#
#     def change_lxd_date(self, new_lxd_date: str):
#         self.clear_and_input_text("lxd_date", new_lxd_date)
#
#     def change_nationality(self, nationality: str):
#         self.select_from_dropdown("nationality_dropdown", nationality)
#
#     def change_marital_status(self, status: str):
#         self.select_from_dropdown("marital_status_dropdown", status)
#
#     def change_birth_date(self, new_birth_date: str):
#         self.clear_and_input_text("birth_date", new_birth_date)
#
#     @allure.step("Нажать кнопку сохранения изменений")
#     def click_save_changes(self):
#         """Сохраняет изменения."""
#         save_button_locator = self.LOCATORS["save_button"]
#         self.wait.until(EC.element_to_be_clickable(save_button_locator)).click()
