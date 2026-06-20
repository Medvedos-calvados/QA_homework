from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        # Поле ввода задержки
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, text):
        # Метод с JavaScript-кликом, чтобы не было ошибки Intercept
        locator = (By.XPATH, f"//span[text()='{text}']")
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def get_result_text(self):
        # Поле результата 
        result_screen = (By.CLASS_NAME, "screen")
        
        # Ждем 45 секунд появления числа 15
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(result_screen, "15")
        )
        
        return self.driver.find_element(*result_screen).text




