from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        wait = WebDriverWait(driver, 15)

        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
            # zip-code сознательно оставляем пустым
        }

        # Шаг 1–2: открываем страницу и заполняем поля по name
        for name, value in fields.items():
            field = wait.until(
                EC.presence_of_element_located((By.NAME, name))
            )
            field.send_keys(value)

        # Шаг 3: нажимаем Submit
        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )
        submit_button.click()

        # После submit мы уже на data-types-submitted.html —
        # ждём, пока скрипт раскрасит блоки
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#zip-code.alert-danger")
            )
        )

        # Шаг 4: Zip code подсвечен красным
        zip_classes = driver.find_element(
            By.ID, "zip-code"
        ).get_attribute("class") or ""
        assert "alert-danger" in zip_classes, (
            f"Zip code не подсвечен красным. Классы: {zip_classes}"
        )

        # Шаг 5: остальные поля подсвечены зелёным
        for name in fields:
            classes = driver.find_element(
                By.ID, name
            ).get_attribute("class") or ""
            assert "alert-success" in classes, (
                f"Поле с id '{name}' не подсвечено зелёным. Классы: {classes}"
            )

    finally:
        driver.quit()