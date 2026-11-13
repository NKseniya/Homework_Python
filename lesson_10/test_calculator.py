import allure

from pages.calculator_page import CalculatorPage


@allure.title("Вычисление 7 + 8 на медленном калькуляторе")
@allure.description(
    "Устанавливает задержку вычисления 45 секунд, нажимает 7 + 8 = "
    "и дожидается появления результата 15 на экране."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.MINOR)
def test_slow_calculator(driver):
    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay("45")

    with allure.step("Нажать кнопки 7, +, 8, ="):
        page.press("7", "+", "8", "=")

    with allure.step("Дождаться результата 15"):
        page.wait_result("15", timeout=120)

    with allure.step("Проверить, что на экране значение 15"):
        assert page.get_result() == "15", (
            f"Ожидалось 15, но получено: {page.get_result()}"
        )
