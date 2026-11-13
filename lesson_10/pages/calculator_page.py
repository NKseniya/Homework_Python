from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


CALCULATOR_URL = (
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
)


class CalculatorPage(BasePage):
    """Page Object медленного калькулятора из набора Selenium examples."""

    DELAY_INPUT: Tuple[str, str] = (By.ID, "delay")
    SCREEN: Tuple[str, str] = (By.CSS_SELECTOR, ".screen")
    BUTTON: str = "//span[normalize-space()='{}']"

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        super().open(CALCULATOR_URL)

    def set_delay(self, seconds: str) -> None:
        """Устанавливает задержку вычисления на калькуляторе.

        Args:
            seconds: значение задержки в секундах в виде строки.
        """
        field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        field.clear()
        field.send_keys(seconds)

    def press(self, *buttons: str) -> None:
        """Нажимает кнопки калькулятора по их подписям.

        Args:
            *buttons: подписи кнопок в порядке нажатия,
            например '7', '+', '8', '='.
        """
        for label in buttons:
            self.click((By.XPATH, self.BUTTON.format(label)))

    def get_result(self) -> str:
        """Возвращает текст с экрана калькулятора.

        Returns:
            Строка с текущим значением на экране.
        """
        return self.find(self.SCREEN).text

    def wait_result(self, expected: str, timeout: int) -> None:
        """Ждёт, пока на экране появится ожидаемое значение.

        Args:
            expected: ожидаемый текст на экране.
            timeout: максимальное время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_result() == expected
        )
