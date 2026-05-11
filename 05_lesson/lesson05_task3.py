from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Открываем Firefox
driver = webdriver.Firefox()

try:
    # 2. ПЕРЕХОДИМ ПО ССЫЛКЕ ИЗ ЗАДАНИЯ
    # Важно: адрес должен быть именно таким, с "the-internet"
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Даем странице 3-5 секунд на загрузку (если интернет медленный)
    time.sleep(5)
    
    # 3. Находим поле ввода (тег input)
    input_field = driver.find_element(By.TAG_NAME, "input")
    
    # 4. Вводим текст 12345
    input_field.send_keys("12345")
    time.sleep(2)
    
    # 5. Очищаем это поле
    input_field.clear()
    time.sleep(2)
    
    # 6. Вводим текст 54321
    input_field.send_keys("54321")
    time.sleep(2)
    
    print("Упражнение 3 успешно выполнено!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 7. Закрываем браузер
    driver.quit()