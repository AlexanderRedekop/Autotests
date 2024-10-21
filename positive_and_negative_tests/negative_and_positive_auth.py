import pytest
from selenium.webdriver.common.by import By
from conftest import driver
from pages.homepage import HomePage


# Выборка паролей и логинов для тестов.
emails = ['TestEmail@gmail.com']                                        # Корректный EMAIL.
passwords = ['QWERTY1!', 'qwerty1!', '!1Qwerty']                        # Список корректных паролей.
not_cor_emails = ['TestEmail', '@gmail.com', '1234@gmail.com', ""]      # Список некорректных EMAIL.
not_cor_passwords = [                                                   # Список некорректных паролей.
'qwerty', 'QWERTY',
'qwe', 'qwertyuiop',
'12345678', '!@#$&',
'qwerty1', 'qwerty!',
"", 'Кириллица'
]

# Функция генерации корректного логина и некорретных паролей.
def generate_pairs():
    pairs = []                # Переменная для списков сгенерированных пар.
    for email in emails:        # Выбор элемента из списка emails.
        for passw in not_cor_passwords:    # Выбор элемента из списка некорректных паролей.
            pairs.append(pytest.param((email, passw), id=f'{email}, {passw}'))  # Создание кортежей из логина и пароля, и их маркировка.
    return pairs  #


# Авторизация с корректными emails + некорректными passwords. (Попарное тестирование)
@pytest.mark.parametrize('creds', generate_pairs())       # Декоратор для параметризации.
def test_n_auth(driver, creds):
    login, pas = creds                # Создание переменных из сгенерированных данных.
    homepage = HomePage(driver)       # Сессия работы со страницей.
    homepage.close_market()           # Закрытие всплывающего окна.
    homepage.click_sign_in_homepage()              # Клик по кнопке с переходом на стр-цу создания акк-та.
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(login)     # Ввод логина.
    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(pas)    # Ввод пароля.
    driver.find_element(By.XPATH, ' //button[@type="submit"]').click()          # Клик по кнопке авторизации.
    print('System displayed message about not corrected pas/email')         # Вывод завершения теста с ответом.

# Генерация некорректных логинов и корректных паролей.
def generate_pairs2():
    pairs = []
    for email in not_cor_emails:
        for passw in passwords:
            pairs.append(pytest.param((email, passw), id=f'{email}, {passw}'))
    return pairs

# Авторизация с некорректными mails + корректными passwords.
@pytest.mark.parametrize('creds', generate_pairs2())
def test_n_auth2(driver, creds):
    login, pas = creds
    homepage = HomePage(driver)
    homepage.close_market()
    homepage.click_sign_in_homepage()
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(login)
    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(pas)
    driver.find_element(By.XPATH, ' //button[@type="submit"]').click()
    print('System demanded to enter a valid email')





