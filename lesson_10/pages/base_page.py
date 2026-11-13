from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц: общая механика Selenium."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу драйвером и явным ожиданием.

        Args:
            driver: экземпляр WebDriver текущего браузера.
        """
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url: str) -> None:
        """Открывает переданный URL в браузере.

        Args:
            url: адрес страницы.
        """
        self.driver.get(url)

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """Находит элемент по локатору с явным ожиданием.

        Args:
            locator: кортеж (способ поиска, значение локатора).

        Returns:
            Найденный элемент WebElement.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: Tuple[str, str]) -> None:
        """Кликает по кликабельному элементу.

        Args:
            locator: кортеж (способ поиска, значение локатора).
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: Tuple[str, str], text: str) -> None:
        """Очищает поле и вводит в него текст.

        Args:
            locator: кортеж (способ поиска, значение локатора).
            text: текст для ввода.
        """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
