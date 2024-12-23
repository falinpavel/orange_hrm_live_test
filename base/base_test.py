import pytest
from pages.auth.login_page import LoginPage
from pages.pages.dashboard_page import DashboardPage
from pages.pages.profile_page import ProfilePage
from pages.sidebar.sidebar_element import SidebarElements
from config.data import Data
from pages.pages.admin_page import AdminPage

"""Аннотация типов для тестов. Делаем тесты мультистраничными."""


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    profile_page: ProfilePage
    sidebar_element: SidebarElements
    admin_page: AdminPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.profile_page = ProfilePage(driver)
        request.cls.sidebar_element = SidebarElements(driver)
        request.cls.admin_page = AdminPage(driver)
