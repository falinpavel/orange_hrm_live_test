from datetime import datetime
from base.base_test import BaseTest
import utils.faker_data as FD
import random
import allure
import pytest


@allure.feature("Profile change")
class TestProfileFeature(BaseTest):
    @allure.title("Change employee info")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_employee_info(self):
        """
        Тест-кейс: Изменение информации о сотруднике:
        1. Открыть главную страницу
        2. Ввести валидный логин
        3. Ввести валидный пароль
        4. Нажать на кнопку "Submit"
        5. Происходит редирект на страницу "Dashboard"
        6. Нажать на выпадающее меню "My Info"
        7. Изменить имя сотрудника
        8. Изменить отчество сотрудника
        9. Изменить фамилию сотрудника
        10. Изменить ID сотрудника
        11. Изменить другой ID сотрудника
        12. Изменить DLN сотрудника
        13. Изменить LXD date сотрудника
        14. Изменить гражданство сотрудниа
        15. Изменить семейное положение сотрудника
        16. Изменить дату рождения сотрудника
        17. Сохранить изменения, нажать на кнопку "Save Changes" (делаем скриншот)
        """
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.click_my_info_link()
        self.profile_page.change_first_name(FD.fake_fio()[0])
        self.profile_page.change_middle_name(FD.fake_fio()[1])
        self.profile_page.change_second_name(FD.fake_fio()[2])
        self.profile_page.change_nickname(FD.fake_nickname())
        self.profile_page.change_employee_id(f"Test{random.randint(1, 100)}")
        self.profile_page.change_other_id(f"Test{random.randint(1, 100)}")
        self.profile_page.change_dln(f"Test{random.randint(1, 100)}")
        self.profile_page.change_lxd_date(new_lxd_date=datetime.now().strftime("%Y-%m-%d"),
                                          other_format=datetime.now().strftime("%d-%m-%Y"))
        self.profile_page.change_nationality()
        self.profile_page.change_marital_status()
        # self.profile_page.change_birth_date(datetime.now().strftime("%d-%m-%Y"))
        self.profile_page.change_gender_radio_button()
        self.profile_page.click_save_changes()
        self.profile_page.make_screenshot("test_change_employee_info")

