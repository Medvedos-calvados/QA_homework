from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Открываем Chrome
driver = webdriver.Chrome()

try:
    # 2. Переходим на страницу
    driver.get("http://uitestingplayground.com/classattr")
    
    # Даем подгрузится
    time.sleep(2)

    # 3. Кликаем на синюю кнопку. 
    blue_button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    
    # 4. После клика появится окно 
    time.sleep(1)
    alert = driver.switch_to.alert
    print(f"Текст в окне: {alert.text}")
    alert.accept()

    print("Скрипт успешно отработал!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()

