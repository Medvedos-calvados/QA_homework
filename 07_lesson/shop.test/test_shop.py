import pytest
from selenium import webdriver
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage, OverviewPage

@pytest.fixture
def driver():
    # Используем Firefox 
    browser = webdriver.Firefox()
    browser.get("https://www.saucedemo.com/")
    yield browser
    # Закрываем браузер СРАЗУ после выполнения шагов 
    browser.quit()

def test_shop_total(driver):
    # Создаем объекты всех страниц
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)

    # Авторизация
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров
    main_page.add_products()

    # Переход в корзину и нажатие Checkout
    main_page.go_to_cart()
    cart_page.checkout()

    # 4. Заполнение формы
    checkout_page.fill_form("Наталья", "Медведева", "123456")

    # Читаем итоговую стоимость 
    # Сохраняем её в обычную переменную-строку
    final_total = overview_page.get_total()
    
    # Проверка 
    expected_price = "Total: $58.29"
    assert final_total == expected_price, f"Ошибка! Ожидали {expected_price}, но получили {final_total}"
