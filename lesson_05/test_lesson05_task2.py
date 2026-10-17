from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submit():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу https://httpbin.qa-territory.online/forms/post
    target_url = "https://httpbin.qa-territory.online/forms/post"
    driver.get(target_url)

    assert target_url in driver.current_url, "Неверный URL после перехода"
    # 2. Найдите поле ввода с названием custname (используем By.NAME)
    custname_field = wait.until(
        EC.presence_of_element_located((By.NAME, "custname"))
    )

    # 3. Введите в него ваше имя (используем send_keys())
    my_name = "Tester"
    custname_field.send_keys(my_name)

    # 4. Найдите кнопку Submit и нажмите на неё (используем By.XPATH по тексту)
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="Submit"]'))
    )
    submit_button.click()

    # 5. Проверьте, что после нажатия URL изменился (driver.current_url)
    assert driver.current_url != target_url, (
     "URL не изменился после отправки формы"
    )

    driver.quit()
