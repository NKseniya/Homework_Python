from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу: https://www.saucedemo.com/ в FireFox.
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуйтесь как пользователь standard_user.
    user_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']")))
    user_name.send_keys("standard_user")
    password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
    password.send_keys("secret_sauce")
    login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_btn.click()

    # 3. Добавьте в корзину товары:
    wait = WebDriverWait(driver, 10)

    button_add_backpack = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
    button_add_backpack.click()

    button_add_t_shirt = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")))
    button_add_t_shirt.click()

    button_add_onesie = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")))
    button_add_onesie.click()


    # 4. Перейдите в корзину.
    basket_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Cart, 3 items']")))
    basket_btn.click()

    # 5.Нажмите Checkout.
    checkout_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='checkout']")))
    checkout_btn.click()

    # 6. Заполните форму своими данными: имя, фамилия, почтовый индекс.
    first_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']")))
    first_name.send_keys("Кирилл")  # Твое имя

    last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
    last_name.send_keys("Гончаров")  # Твоя фамилия

    postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    postal_code.send_keys("457351")  # Твой почтовый индекс.

    # 7. Нажмите кнопку Continue.
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']")))
    continue_button.click()

    # 8. Прочитайте со страницы итоговую стоимость (Total).
    total_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='summary_total_label']")))
    total_text = total_element.text

    # 9. Закройте браузер. Проверьте, что итоговая сумма равна $58.29.
    assert total_text == "Total: $58.29", f"Ожидалось 'Total: $58.29', но получено: {total_text}"

    driver.quit()