from selenium.webdriver.common.by import By

class CreateAccount:

    # Инициализация класса.
    def __init__(self, driver):
        self.driver = driver

    # Ввод корректных данных при регистрации во всех полях.
    def enter_data(self):
        self.driver.find_element(By.XPATH, '//input[@name="nameFirst"]').send_keys('TestName')
        self.driver.find_element(By.XPATH, '//input[@name="nameLast"]').send_keys('TestLastName')
        self.driver.find_element(By.XPATH, '// input[@name="email"]').send_keys('TestEmail@gmail.com')
        self.driver.find_element(By.XPATH, '// input[@name="phone"]').send_keys(89999999999)

    # Ввод корректных данных при регистрации, кроме телефона. (Телефон заполнять необязательно)
    def enter_data2(self):
        self.driver.find_element(By.XPATH, '//input[@name="nameFirst"]').send_keys('TestName123')
        self.driver.find_element(By.XPATH, '//input[@name="nameLast"]').send_keys('TestLastName321')
        self.driver.find_element(By.XPATH, '// input[@name="email"]').send_keys('TestEmail23@gmail.com')
        self.driver.find_element(By.XPATH, '// input[@name="phone"]').send_keys("")

    # Ввод некорректных данных при регистрации. (Не заполнено поле "Имя")
    def incor_enter_data(self):
        self.driver.find_element(By.XPATH, '//input[@name="nameFirst"]').send_keys("")
        self.driver.find_element(By.XPATH, '//input[@name="nameLast"]').send_keys('TestLastName')
        self.driver.find_element(By.XPATH, '// input[@name="email"]').send_keys('TestEmail@gmail.com')
        self.driver.find_element(By.XPATH, '// input[@name="phone"]').send_keys(89999999999)

    # Ввод некорректных данных при регистрации. (Не заполнено поле "Фамилия")
    def incor_enter_data2(self):
        self.driver.find_element(By.XPATH, '//input[@name="nameFirst"]').send_keys('TestName')
        self.driver.find_element(By.XPATH, '//input[@name="nameLast"]').send_keys("")
        self.driver.find_element(By.XPATH, '// input[@name="email"]').send_keys('TestEmail@gmail.com')
        self.driver.find_element(By.XPATH, '// input[@name="phone"]').send_keys(89999999999)

    # Ввод некорректных данных при регистрации. (Не заполнено поле "Почта")
    def incor_enter_data3(self):
        self.driver.find_element(By.XPATH, '//input[@name="nameFirst"]').send_keys('TestName')
        self.driver.find_element(By.XPATH, '//input[@name="nameLast"]').send_keys('TestLastName')
        self.driver.find_element(By.XPATH, '// input[@name="email"]').send_keys("")
        self.driver.find_element(By.XPATH, '// input[@name="phone"]').send_keys(89999999999)

    #    Ввод некорректных данных при регистрации. (Поле почта заполнена без почтового ящика)
    def incor_enter_data4(self):
        self.driver.find_element(By.XPATH, '//input[@name="nameFirst"]').send_keys("TestName")
        self.driver.find_element(By.XPATH, '//input[@name="nameLast"]').send_keys("TestLastName")
        self.driver.find_element(By.XPATH, '// input[@name="email"]').send_keys("TestEmail")
        self.driver.find_element(By.XPATH, '// input[@name="phone"]').send_keys(89999999999)

    # Нажатие на кнопку "Создать аккаунт".
    def click_create_ca(self):
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Create Account")]').click()











