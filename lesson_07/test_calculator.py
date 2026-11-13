from pages.calculator_page import CalculatorPage


def test_slow_calculator(driver):
    page = CalculatorPage(driver)

    # 1. Открываем страницу калькулятора
    page.open()

    # 2. Вводим задержку 45 секунд
    page.set_delay("45")

    # 3. Нажимаем кнопки: 7, +, 8, =
    page.press("7", "+", "8", "=")

    # 4. Ждём результат 15 (появится примерно через 45 секунд)
    page.wait_result("15", timeout=120)

    assert page.get_result() == "15", (
        f"Ожидалось 15, но получено: {page.get_result()}"
    )
