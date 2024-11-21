"""Храним фикстуры для тестов."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True) # autouse=True || scope="function" - запуск драйвера для каждого теста отдельно
def driver_init(request):
    """Инициализация драйвера."""
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver # данная конструкция позволяет использовать драйвер в тестовых классах
    yield driver
    driver.quit()