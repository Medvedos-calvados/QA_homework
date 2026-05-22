
import pytest
from selenium import webdriver
from calc_page import CalcPage

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    # Закрываем браузер СРАЗУ после получения результата
    browser.quit()

def test_slow_calculator(driver):
    page = CalcPage(driver)
    
    page.open()
    # Вводим 45 в поле над калькулятором
    page.set_delay("45")
    
    # Нажимаем кнопки
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    
    # Сохраняем результат 
    final_result = page.get_result_text()
    
    # Проверяем. Браузер закроется, и pytest покажет результат.
    assert final_result == "15", f"Ошибка! Ожидали 15, а на табло видим {final_result}"

