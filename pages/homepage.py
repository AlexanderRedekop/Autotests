from selenium.webdriver.common.by import By

class HomePage:

    # Инициализация класса.
    def __init__(self, driver):
        self.driver = driver

    # Закрытие всплывающего окна.
    def close_market(self):
        self.driver.find_element(By.ID, 'popup-widget238491-close-icon').click()

    # Переход на страницу с регистрацией.
    def click_create_homepage(self):
        self.driver.find_element(By.ID, '4').click()
        self.driver.find_element(By.XPATH, '//a[contains(text(), "Create Account")]').click()

    # Переход на страницу с авторизацией.
    def click_sign_in_homepage(self):
        self.driver.find_element(By.ID, '4').click()
        self.driver.find_element(By.ID, 'n-238369238407-membership-sign-in').click()


