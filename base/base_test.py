import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.profile_page import ProfilePage
from pages.sidebar_element import SidebarElements
from config.data import Data

"""Аннотация типов для тестов. Делаем тесты мультистраничными."""


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    profile_page: ProfilePage
    sidebar_element: SidebarElements

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.profile_page = ProfilePage(driver)
        request.cls.sidebar_element = SidebarElements(driver)
