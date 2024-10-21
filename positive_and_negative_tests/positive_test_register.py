from conftest import driver
from pages.homepage import HomePage
from pages.create_account_page import CreateAccount

# Регистрация с корректным заполнением всех полей.
def test_reg(driver):
    homepage = HomePage(driver)                   # Сессия работы со страницей.
    homepage.close_market()                       # Закрытие всплывающего окна.
    homepage.click_create_homepage()              # Клик по кнопке с переходом на стр-цу создания акк-та.
    create_account_page = CreateAccount(driver)   # Сессия работы со страницей.
    create_account_page.enter_data()              # Ввод данных.
    create_account_page.click_create_ca()         # Клик по кнопке создания акк-та.
    print('User is registered')                   # Вывод завершения теста с ответом.

# Регистрация с корректным заполнением всех полей, кроме телефона. (Телефон заполнять необязательно)
def test_reg2(driver):
    homepage = HomePage(driver)
    homepage.close_market()
    homepage.click_create_homepage()
    create_account_page = CreateAccount(driver)
    create_account_page.enter_data2()
    create_account_page.click_create_ca()
    print('User is registered')

