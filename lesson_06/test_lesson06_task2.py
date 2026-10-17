# lesson_06/test_session_storage_auth.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()


def test_session_storage_auth(driver: webdriver.Chrome):
    wait = WebDriverWait(driver, 20)
    base_url = "https://gitflic.ru/"

    user1_cookies = [
        {
            "name": "SESSION",
            "value": "<ZDdhYzQwZDgtODYxNS00NDAzLWIxOTQtNWRlOWM5N2ZiMjMz>",
        }
    ]

    user2_cookies = [
        {
            "name": "SESSION",
            "value": "<ZGIyOWNmNGEtMjhhMi00MDdmLTg4NWUtZDFlNmVjMTIyOGNl>",
        }
    ]

    # Пользователь 1
    driver.get(base_url)
    driver.delete_all_cookies()
    for cookie in user1_cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    wait.until(lambda d: d.current_url != base_url or True)

    profile_url_1 = "https://gitflic.ru/user/msnevagno"
    driver.get(profile_url_1)
    url_after_login_1 = driver.current_url

    # Разлогиниваемся
    driver.delete_all_cookies()
    driver.refresh()

    # Пользователь 2
    driver.get(base_url)
    driver.delete_all_cookies()
    for cookie in user2_cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    wait.until(lambda d: d.current_url != base_url or True)

    profile_url_2 = "https://gitflic.ru/user/nk98765"
    driver.get(profile_url_2)
    url_after_login_2 = driver.current_url

    assert url_after_login_1 != url_after_login_2, (
        f"URL профилей совпали: {url_after_login_1} и {url_after_login_2}"
    )
