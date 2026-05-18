from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def test_form_validation():
    # 1. Настройка браузера Edge
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    
    # Разворачиваем на весь экран, чтобы элементы не перекрывали друг друга
    driver.maximize_window()
    
    try:
        # 2. Переход на страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # 3. Заполнение полей данными
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")
        
        # Поле Zip code оставляем пустым
        driver.find_element(By.NAME, "zip-code").clear()

        # 4. Нажатие кнопки Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # Прокручиваем страницу до кнопки перед кликом
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        
        # Проверяем, что Zip code подсвечен КРАСНЫМ 
        zip_field = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_field.get_attribute("class")

        # Проверяем, что остальные поля подсвечены ЗЕЛЕНЫМ 
        success_fields = [
            "first-name", "last-name", "address", "e-mail", 
            "phone", "city", "country", "job-position", "company"
        ]
        
        for field_id in success_fields:
            field_element = driver.find_element(By.ID, field_id)
            field_class = field_element.get_attribute("class")
            assert "alert-success" in field_class

    finally:
        # 6. Закрытие браузера
        driver.quit()