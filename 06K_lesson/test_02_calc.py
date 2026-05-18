from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    driver = webdriver.Chrome()
    # 1. Разворачиваем на весь экран
    driver.maximize_window()
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. Настраиваем ожидание
        wait = WebDriverWait(driver, 60)

        # 3. Вводим задержку
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 4. Функция для "умного" клика (чтобы не дублировать код)
        def smart_click(xpath):
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()

        # 5. Нажимаем кнопки через умный клик
        smart_click("//span[text()='7']")
        smart_click("//span[text()='+']")
        smart_click("//span[text()='8']")
        smart_click("//span[text()='=']")

        # 6. Ждем результата (до 60 секунд)
        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        # 7. Проверка
        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15"

    finally:
        driver.quit()

