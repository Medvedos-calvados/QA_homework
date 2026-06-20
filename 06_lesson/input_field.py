from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Запуск браузера
driver = webdriver.Chrome()

try:
    # 2. Переход на нужную страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Создаем объект ожидания на 10 секунд
    wait = WebDriverWait(driver, 10)

    # 3. Поиск поля ввода и ввод текста "SkyPro"
    # Находим поле по его ID 'newButtonName'
    input_field = wait.until(
        EC.element_to_be_clickable((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    # 4. Поиск синей кнопки и клик по ней
    # Используем ID 'updatingButton'
    updating_button = driver.find_element(By.ID, "updatingButton")
    updating_button.click()

    # 5. Получение нового текста кнопки и вывод в консоль
    # После клика текст кнопки должен измениться на тот, что мы ввели
    new_button_text = updating_button.text
    print(new_button_text)

finally:
    # 6. Закрытие браузера
    driver.quit()