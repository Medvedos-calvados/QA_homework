import pytest
import allure
from selenium import webdriver
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage, OverviewPage
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get("https://www.saucedemo.com/")
    yield browser
    browser.quit()

@allure.title("Проверка итоговой стоимости интернет-заказа")
@allure.description("Тест авторизуется, добавляет три товара в корзину, оформляет заказ и сверяет финальную стоимость")
@allure.feature("Магазин")
@allure.severity("blocker")
def test_shop_total(driver: WebDriver) -> None:
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)

    login_page.login("standard_user", "secret_sauce")
    main_page.add_products()
    main_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_form("Наталья", "Медведева", "123456")
    
    final_total = overview_page.get_total()
    
    expected_price = "Total: $58.29"
    with allure.step(f"Проверить, что итоговая сумма равна '{expected_price}'"):
        assert final_total == expected_price, f"Ошибка! Ожидали {expected_price}, но получили {final_total}"
