from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализируем драйвер (открываем Chrome)
driver = webdriver.Chrome()

try:
    # 2. Переходим на сайт с загружающимися картинками
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # 3. Настраиваем ожидание
    # Нам нужно подождать, пока все картинки появятся. 10 секунд хватит с запасом.
    wait = WebDriverWait(driver, 10)
    
    # Ждем, пока на странице появится хотя бы один элемент с тегом 'img' по ID контейнера
    # На этом сайте картинки появляются в блоке с id="image-container"
    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

    # 4. Находим все картинки на странице
    # Метод find_elements (во множественном числе) возвращает список всех найденных объектов
    images = driver.find_elements(By.TAG_NAME, "img")

    # 5. Получаем 3-ю картинку
    # В программировании списки начинаются с 0, поэтому:
    # [0] - первая, [1] - вторая, [2] - ТРЕТЬЯ.
    third_image = images[2]

    # 6. Берем у этой картинки значение атрибута 'src' (ссылку на файл)
    src_url = third_image.get_attribute("src")

    # 7. Выводим результат в консоль
    print(src_url)

finally:
    # 8. Закрываем браузер, чтобы не оставлять лишних процессов
    driver.quit()