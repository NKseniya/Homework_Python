from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    start_url = "https://httpbin.qa-territory.online"
    driver.get(start_url)

    # Проверка, что мы на стартовой странице
    assert driver.current_url == start_url, "URL не совпадает со стартовым"

    # Поиск ссылки по тексту "HTML Form" через By.LINK_TEXT
    html_form_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "HTML Form"))
    )
    html_form_link.click()

    # Проверка, что URL содержит /forms/post
    expected_path = "/forms/post"
    assert expected_path in driver.current_url, (

         "URL не перешёл на страницу формы"
    )

    # Возврат назад и проверка возврата на главную
    driver.back()
    assert driver.current_url == start_url, "Не вернулся на стартовую страницу"

    driver.quit()
