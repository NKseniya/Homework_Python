from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

CALCULATOR_URL = (
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
)


class CalculatorPage(BasePage):
    # Локаторы собраны в одном месте
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")
    BUTTON = "//span[normalize-space()='{}']"

    def open(self):
        super().open(CALCULATOR_URL)

    def set_delay(self, seconds: str):
        field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        field.clear()
        field.send_keys(seconds)

    def press(self, *buttons: str):
        """Нажимает кнопки калькулятора по их подписям."""
        for label in buttons:
            self.click((By.XPATH, self.BUTTON.format(label)))

    def get_result(self) -> str:
        return self.find(self.SCREEN).text

    def wait_result(self, expected: str, timeout: int):
        """Ждёт, пока на экране появится ожидаемое значение."""
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_result() == expected
        )
