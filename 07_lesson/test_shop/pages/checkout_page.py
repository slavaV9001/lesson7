from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Локаторы
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    def fill_first_name(self, first_name):
        field = self.wait.until(
            EC.element_to_be_clickable(self.first_name_input)
        )
        field.send_keys(first_name)

    def fill_last_name(self, last_name):
        field = self.wait.until(
            EC.element_to_be_clickable(self.last_name_input)
        )
        field.send_keys(last_name)

    def fill_postal_code(self, postal_code):
        field = self.wait.until(
            EC.element_to_be_clickable(self.postal_code_input)
        )
        field.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_button.click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.total_price)
        )
        return total_element.text
