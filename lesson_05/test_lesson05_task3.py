from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    url = "https://httpbin.qa-territory.online/links/10"
    driver.get(url)

    # Ждём, пока появятся все ссылки (чтобы не полагаться на time.sleep)
    links = wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
    )

    # Проверяем, что количество ссылок равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"

    # Проверяем, что все ссылки отображаются на странице
    for link in links:
        assert link.is_displayed(), (
         "Одна из ссылок не отображается на странице"
        )

    # Проверяем, что текст первой ссылки содержит "1"
    first_link_text = links[0].text
    assert "1" in first_link_text, (
        f"Текст первой ссылки не содержит '1'. Получено: '{first_link_text}'"
    )

    driver.quit()
