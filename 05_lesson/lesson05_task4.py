from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    # 1. Перейти на страницу
    driver.get("http://the-internet.herokuapp.com/login")
    
    # 2. Ввести логин и пароль
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # 3. Нажать кнопку Login
    driver.find_element(By.TAG_NAME, "button").click()
    
    # 4. Вывести текст с зеленой плашки
    success_message = driver.find_element(By.ID, "flash").text
    print(f"Задание 4: Текст сообщения — {success_message}")

finally:
    # 5. Закрыть браузер
    driver.quit()