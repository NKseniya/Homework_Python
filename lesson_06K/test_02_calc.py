import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    service = webdriver.ChromeService(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)
    yield d
    d.quit()


def test_slow_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)
    # Даём 120 секунд, так как калькулятор реально медленный
    wait = WebDriverWait(driver, 120)
    print(f"Открываем страницу: {url}")

    # 1. Вводим 45 в поле #delay
    delay_input = wait.until(
        EC.element_to_be_clickable((By.ID, "delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")
    print("✅ Введено значение 45 в поле задержки")

    # ВАЖНО: В этом HTML нет кнопки "Set delay".
    # Задержка срабатывает автоматически после ввода числа.
    # Просто ждём, чтобы страница поняла, что мы ввели 45.
    wait.until(lambda d: d.find_element(By.ID, "delay")
               .get_attribute("value") == "45"
               )

    # 2. Нажимаем кнопки: 7, +, 8, =
    # Так как кнопки - это <span> без ID, ищем их по тексту
    buttons_to_click = [
        ("7", "//span[normalize-space()='7']"),
        ("+", "//span[normalize-space()='+']"),
        ("8", "//span[normalize-space()='8']"),
        ("=", "//span[normalize-space()='=']")
    ]

    for label, xpath in buttons_to_click:
        btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        btn.click()
        print(f"Нажата кнопка: {label}")

    # 3. Ждём появления результата 15 в блоке .screen
    result_locator = (By.CSS_SELECTOR, ".screen")

    # Ждём, пока текст станет равен "15"
    wait.until(
        lambda d: d.find_element(*result_locator).text == "15"
    )

    result_text = driver.find_element(*result_locator).text
    assert result_text == "15", f"Ожидалось 15, но получено: {result_text}"

    print("✅ Результат верный: 15")
    print("🎉 Тест успешно пройден!")
    driver.quit()
