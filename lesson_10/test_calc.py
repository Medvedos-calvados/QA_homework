import allure
import pytest
from selenium import webdriver
from calc_page import CalcPage


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера Chrome."""
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет операцию сложения 7 + 8 с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver):
    """Тест проверяет сложение чисел с выставленной задержкой анимации."""
    page = CalcPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Ввести 45 в поле задержки над калькулятором"):
        page.set_delay("45")

    with allure.step("Нажать кнопки '7', '+', '8', '='"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Дождаться результата и проверить, что он равен 15"):
        final_result = page.get_result_text()
        assert final_result == "15", (
            f"Ошибка! Ожидали 15, а на табло видим {final_result}"
        )
