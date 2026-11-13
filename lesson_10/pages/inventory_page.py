from typing import Tuple

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage:
    """Page Object каталога товаров интернет-магазина."""

    ADD_BUTTON: str = "add-to-cart-{}"
    CART_LINK: Tuple[str, str] = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE: Tuple[str, str] = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver) -> None:
        """Инициализирует страницу каталога.

        Args:
            driver: экземпляр WebDriver текущего браузера.
        """
        self.page = BasePage(driver)

    def add_product(self, product_id: str) -> None:
        """Добавляет товар в корзину по его идентификатору.

        Args:
            product_id: идентификатор товара, например
                'sauce-labs-backpack'.
        """
        self.page.click((By.ID, self.ADD_BUTTON.format(product_id)))

    def open_cart(self) -> None:
        """Открывает страницу корзины."""
        self.page.click(self.CART_LINK)

    def get_cart_badge_text(self) -> str:
        """Возвращает число товаров на значке корзины.

        Returns:
            Строка с количеством товаров в корзине.
        """
        return self.page.find(self.CART_BADGE).text
