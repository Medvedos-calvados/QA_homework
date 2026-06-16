import allure
import pytest
from selenium import webdriver
from calc_page import CalcPage


@pytest.fixture
def driver_calc():
    """Фикстура для инициализации браузера Firefox для тестов калькулятора."""
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет операцию сложения 7 + 8 с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator_sum(driver_calc):
    """Тест проверяет сложение чисел с выставленной задержкой."""
    calc_page = CalcPage(driver_calc)

    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()

    with allure.step("Установить задержку вычислений в 45 секунд"):
        calc_page.set_delay("45")

    with allure.step("Ввести математическое выражение '7 + 8 ='"):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Дождаться результата и проверить, что он равен 15"):
        result = calc_page.get_result_text()
        assert result == "15", f"Ожидалось 15, но калькулятор показал {result}"
