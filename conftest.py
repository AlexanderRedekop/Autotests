from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

# Создание предусловия. (Открытие браузера и сайта)
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()    # Полный размер экрана у браузера.
    driver.implicitly_wait(10)  # Неявное ожидание
    driver.get('https://candymapper.com/')  # Открытие сайта
    yield driver  # Возвращение созданного браузера.

