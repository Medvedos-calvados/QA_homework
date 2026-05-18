from selenium import webdriver
from selenium.webdriver.common.by import By

def test_shop_purchase():
    # 1. Открываем Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        # 2. Переход на сайт и авторизация
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавление товаров в корзину
        # Ищем кнопки добавления по ID товаров
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # 4. Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 5. Нажимаем Checkout
        driver.find_element(By.ID, "checkout").click()

        # 6. Заполнение формы 
        driver.find_element(By.ID, "first-name").send_keys("Natali")
        driver.find_element(By.ID, "last-name").send_keys("Medvedeva")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # 7. Нажимаем Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Получаем итоговую стоимость (Total)
        # Ищем элемент с классом summary_total_label
        total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        
        # 9. Проверка итоговой суммы
        assert total_price == "Total: $58.29"

    finally:
        driver.quit()
