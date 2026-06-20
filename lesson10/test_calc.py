import pytest
import allure
from selenium import webdriver
from calc_page import CalcPage
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет сложение 7 + 8 с задержкой и валидирует результат 15")
@allure.feature("Калькулятор")
@allure.severity("critical")
def test_slow_calculator(driver: WebDriver) -> None:
    page = CalcPage(driver)
    
    page.open()
    page.set_delay("45")
    
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    
    final_result = page.get_result_text()
    
    with allure.step("Проверить, что итоговый результат равен 15"):
        assert final_result == "15", f"Ошибка! Ожидали 15, а на табло видим {final_result}"
