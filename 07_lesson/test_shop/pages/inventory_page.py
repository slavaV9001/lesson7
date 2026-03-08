from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Локаторы
        self.backpack_add_button = (
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-backpack']"
            )
        self.bolt_tshirt_add_button = (
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-bolt-t-shirt']"
            )
        self.onesie_add_button = (
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-onesie']"
            )
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.backpack_add_button)
        )
        button.click()

    def add_bolt_tshirt_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.bolt_tshirt_add_button)
        )
        button.click()

    def add_onesie_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.onesie_add_button)
        )
        button.click()

    def go_to_cart(self):
        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        )
        cart_link.click()
