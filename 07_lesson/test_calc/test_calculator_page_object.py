import pytest
from selenium import webdriver
from PageObject import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calc = CalculatorPage(driver)
    calc.open()
    calc.set_delay("45")
    # нажимаем кнопки
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")
    # результат
    final_result = calc.get_result_text(45)

    assert final_result == "15"
