from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, text):
        button_xpath = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_xpath).click()

    def get_result_text(self, wait_time):
        WebDriverWait(self.driver, wait_time + 5).until(
            EC.text_to_be_present_in_element(self.result_display, "15"))
        return self.driver.find_element(*self.result_display).text
