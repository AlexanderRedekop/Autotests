from conftest import driver
from pages.create_account_page import CreateAccount
from pages.homepage import HomePage


# Регистрация без заполнения поля "Имя".
def test_n_reg1(driver):
    homepage = HomePage(driver)                    # Сессия работы со страницей.
    homepage.close_market()                        # Закрытие всплывающего окна.
    homepage.click_create_homepage()               # Клик по кнопке с переходом на стр-цу создания акк-та.
    create_account_page = CreateAccount(driver)    # Сессия работы со страницей.
    create_account_page.incor_enter_data()         # Ввод данных.
    create_account_page.click_create_ca()          # Клик по кнопке создания акк-та.
    print('System demanded to enter a name')       # Вывод завершения теста с ответом.

# Регистрация без заполнения поля "Фамилия".
def test_n_reg2(driver):
    homepage = HomePage(driver)
    homepage.close_market()
    homepage.click_create_homepage()
    create_account_page = CreateAccount(driver)
    create_account_page.incor_enter_data2()
    create_account_page.click_create_ca()
    print('System demanded to enter a last name')

# Регистрация без заполнения поля "Почта".
def test_n_reg3(driver):
    homepage = HomePage(driver)
    homepage.close_market()
    homepage.click_create_homepage()
    create_account_page = CreateAccount(driver)
    create_account_page.incor_enter_data3()
    create_account_page.click_create_ca()
    print('System demanded to enter a valid email')

# Регистрация с заполнением поля "Почта" некорректной почтой.
def test_n_reg4(driver):
    homepage = HomePage(driver)
    homepage.close_market()
    homepage.click_create_homepage()
    create_account_page = CreateAccount(driver)
    create_account_page.incor_enter_data4()
    create_account_page.click_create_ca()
    print('System demanded to enter a email_2')

