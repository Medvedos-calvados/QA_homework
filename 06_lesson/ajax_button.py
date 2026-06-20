from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Настройка браузера
# Создаем экземпляр драйвера (в данном случае Chrome)
driver = webdriver.Chrome()

try:
    # 2. Переход на нужную страницу
    driver.get("http://uitestingplayground.com/ajax")

     # Создаем один объект ожидания на 20 секунд
    wait = WebDriverWait(driver, 20)

    # 2. Ждем, пока синяя кнопка станет кликабельной, и только потом кликаем
    # Это исправит ошибку NoSuchElementException
    blue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    blue_button.click()

    # 3. Ждем появления зеленой плашки
    # Используем CSS-селектор для поиска класса bg-success
    success_banner = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    # 4. Выводим текст в консоль
    print(success_banner.text)

finally:
    driver.quit()