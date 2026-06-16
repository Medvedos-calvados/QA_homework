from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def login(self, user: str, pwd: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.ID, "login-button").click()


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def add_products(self) -> None:
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()


class OverviewPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def get_total(self) -> str:
        selector = "[data-test='total-label']"
        total_text = self.driver.find_element(By.CSS_SELECTOR, selector).text
        return total_text
