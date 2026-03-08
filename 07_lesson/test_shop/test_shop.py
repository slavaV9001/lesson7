import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


def test_shop_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Открываем сайт
    login_page.open()

    # Авторизуемся
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Добавляем товары в корзину
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()

    # Переходим в корзину
    inventory_page.go_to_cart()
    cart_page.click_checkout()

    # Заполняем данные
    checkout_page.fill_first_name("Имя")
    checkout_page.fill_last_name("Фамилия")
    checkout_code = "123456"
    checkout_page.fill_postal_code(checkout_code)
    checkout_page.click_continue()

    # Проверка итоговой суммы
    total_text = checkout_page.get_total_price()
    assert "58.29" in total_text, f"Ожидалось $58.29, получили {total_text}"
    print("Тест пройден! Итоговая сумма верна.")
