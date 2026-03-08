from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Локаторы
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.element_to_be_clickable(self.username_input)
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.element_to_be_clickable(self.password_input)
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()
