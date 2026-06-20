from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для управления элементами страницы авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу авторизации с веб-драйвером."""
        self.driver = driver

    def login(self, user: str, pwd: str) -> None:
        """Выполняет вход в систему под указанными данными.

        Args:
            user (str): Имя пользователя.
            pwd (str): Пароль пользователя.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.ID, "login-button").click()


class MainPage:
    """Класс для управления элементами главной страницы магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует главную страницу с веб-драйвером."""
        self.driver = driver

    def add_products(self) -> None:
        """Добавляет три определенных товара в корзину покупок."""
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
        """Выполняет переход на страницу корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    """Класс для управления элементами страницы корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу корзины с веб-драйвером."""
        self.driver = driver

    def checkout(self) -> None:
        """Нажимает на кнопку перехода к оформлению заказа."""
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    """Класс для страницы ввода персональных данных покупателя."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу ввода данных с веб-драйвером."""
        self.driver = driver

    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        """Заполняет форму личными данными и переходит далее.

        Args:
            first (str): Имя покупателя.
            last (str): Фамилия покупателя.
            zip_code (str): Почтовый индекс.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()


class OverviewPage:
    """Класс для финальной страницы подтверждения заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу подтверждения с веб-драйвером."""
        self.driver = driver

    def get_total(self) -> str:
        """Считывает и возвращает итоговую стоимость заказа.

        Returns:
            str: Строка с текстом итоговой цены.
        """
        selector = "[data-test='total-label']"
        total_text = self.driver.find_element(By.CSS_SELECTOR, selector).text
        return total_text
