import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalcPage:
    """Класс для управления элементами страницы медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу калькулятора с веб-драйвером.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.url: str = (
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Открыть страницу медленного калькулятора")
    def open(self) -> None:
        """Открывает страницу медленного калькулятора в браузере."""
        self.driver.get(self.url)

    @allure.step("Установить время задержки: {seconds} сек.")
    def set_delay(self, seconds: str) -> None:
        """Устанавливает время задержки анимации калькулятора.

        Args:
            seconds (str): Время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    @allure.step("Нажать кнопку калькулятора: '{text}'")
    def click_button(self, text: str) -> None:
        """Находит кнопку по тексту и выполняет клик через JavaScript.

        Args:
            text (str): Текст на кнопке калькулятора (например, '7', '+').
        """
        locator = (By.XPATH, f"//span[text()='{text}']")
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Получить итоговый результат с экрана")
    def get_result_text(self) -> str:
        """Ожидает появления результата и возвращает его текст с экрана.

        Returns:
            str: Строка с итоговым значением вычислений (ожидается '15').
        """
        result_screen = (By.CLASS_NAME, "screen")

        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(result_screen, "15")
        )

        return self.driver.find_element(*result_screen).text
