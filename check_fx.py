from selenium import webdriver

# Если Firefox установлен, эта команда откроет пустое окно браузера
driver = webdriver.Firefox()
driver.get("https://google.com")
print("Firefox успешно запущен!")
driver.quit()

from selenium import webdriver
import time  # Добавляем библиотеку для пауз

driver = webdriver.Firefox()
driver.get("https://google.com")

print("Firefox запущен. У тебя есть 5 секунд, чтобы на него посмотреть!")
time.sleep(5)  # Программа подождет 5 секунд перед закрытием

driver.quit()