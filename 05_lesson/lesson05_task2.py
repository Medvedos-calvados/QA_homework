from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 1. Настройки, чтобы игнорировать ошибки безопасности
options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

try:
    # 2. Заходим на главную страницу (ту, что на твоем скрине)
    driver.get("http://uitestingplayground.com")
    
    # 3. Сами находим ссылку на нужное задание и кликаем по ней
    link = driver.find_element(By.LINK_TEXT, "Dynamic ID")
    link.click()
    
    # Даем секунду подгрузиться
    time.sleep(2)
    
    # 4. Теперь ищем синюю кнопку по тексту
    blue_button = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]')
    blue_button.click()
    
    print("Задание 2: Клик по кнопке выполнен успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    time.sleep(2)
    driver.quit()