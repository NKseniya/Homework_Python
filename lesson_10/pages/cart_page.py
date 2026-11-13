from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage:
    """Page Object страницы корзины."""

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver) -> None:
        """Инициализирует страницу корзины.

        Args:
            driver: экземпляр WebDriver текущего браузера.
        """
        self.page = BasePage(driver)

    def checkout(self) -> None:
        """Нажимает кнопку Checkout для перехода к оформлению заказа."""
        self.page.click(self.CHECKOUT_BUTTON)
