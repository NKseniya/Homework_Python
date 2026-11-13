from selenium.webdriver.common.by import By

from pages.base_page import BasePage

SHOP_URL = "https://www.saucedemo.com/"


class LoginPage:
    """Page Object страницы авторизации интернет-магазина."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver) -> None:
        """Инициализирует страницу авторизации.

        Args:
            driver: экземпляр WebDriver текущего браузера.
        """
        self.page = BasePage(driver)

    def open(self) -> None:
        """Открывает главную страницу магазина."""
        self.page.open(SHOP_URL)

    def login(self, username: str, password: str) -> None:
        """Вводит логин и пароль и нажимает кнопку входа.

        Args:
            username: логин пользователя.
            password: пароль пользователя.
        """
        self.page.type_text(self.USERNAME_INPUT, username)
        self.page.type_text(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
