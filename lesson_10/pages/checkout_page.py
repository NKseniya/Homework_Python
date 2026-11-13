from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage:
    """Page Object страницы оформления заказа."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver) -> None:
        """Инициализирует страницу оформления заказа.

        Args:
            driver: экземпляр WebDriver текущего браузера.
        """
        self.page = BasePage(driver)

    def fill_customer_info(self, first_name: str, last_name: str,
                           postal_code: str) -> None:
        """Заполняет форму данными покупателя.

        Args:
            first_name: имя покупателя.
            last_name: фамилия покупателя.
            postal_code: почтовый индекс покупателя.
        """
        self.page.type_text(self.FIRST_NAME_INPUT, first_name)
        self.page.type_text(self.LAST_NAME_INPUT, last_name)
        self.page.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def continue_to_overview(self) -> None:
        """Нажимает кнопку Continue для перехода к обзору заказа."""
        self.page.click(self.CONTINUE_BUTTON)

    def get_total_text(self) -> str:
        """Возвращает текст итоговой стоимости (Total).

        Returns:
            Строка вида 'Total: $58.29'.
        """
        return self.page.find(self.TOTAL_LABEL).text
