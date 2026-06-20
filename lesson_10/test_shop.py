import allure
import pytest
from selenium import webdriver
from pages import (
    LoginPage,
    MainPage,
    CartPage,
    CheckoutPage,
    OverviewPage,
)


@pytest.fixture
def driver():
    """Фикстура для инициализации браузера Firefox."""
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get("https://saucedemo.com")
    yield browser
    browser.quit()


@allure.title("Проверка итоговой суммы заказа в магазине")
@allure.description("Тест проверяет сквозной сценарий покупки товаров")
@allure.feature("Оформление заказа (Checkout)")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(driver):
    """Тест проверяет корректность расчета финальной стоимости 3-х товаров."""
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)

    with allure.step("Авторизоваться под стандартным пользователем"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить 3 конкретных товара в корзину"):
        main_page.add_products()

    with allure.step("Перейти в корзину и нажать кнопку Checkout"):
        main_page.go_to_cart()
        cart_page.checkout()

    with allure.step("Заполнить форму покупателя данными"):
        checkout_page.fill_form("Наталья", "Медведева", "123456")

    with allure.step("Проверить, что итоговая стоимость совпадает"):
        final_total = overview_page.get_total()
        expected_price = "Total: $58.29"
        assert final_total == expected_price, (
            f"Ошибка! Ожидали {expected_price}, но получили {final_total}"
        )
