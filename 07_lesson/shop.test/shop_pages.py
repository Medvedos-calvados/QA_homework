from selenium.webdriver.common.by import By

# Страница логина
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, user, pwd):
        # Находим поля по ID и вводим данные
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.ID, "login-button").click()

# Главная страница (Магазин)
class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_products(self):
        # Добавляем 3 конкретных товара по их ID
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        # Кликаем на иконку корзины
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Страница корзины
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        # Нажимаем кнопку оформления заказа
        self.driver.find_element(By.ID, "checkout").click()

# Страница ввода данных покупателя
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first, last, zip_code):
        # Заполняем имя, фамилию и индекс
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

# 5. Страница подтверждения (где цена)
class OverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total(self):
        total_text = self.driver.find_element(By.CSS_SELECTOR, "[data-test='total-label']").text
        return total_text
