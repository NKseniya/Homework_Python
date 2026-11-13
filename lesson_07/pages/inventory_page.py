from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    # Ссылка на корзину: до добавления товаров подпись просто "Cart"
    CART_LINK = (By.XPATH, "//a[contains(@aria-label, 'Cart')]")

    ADD_BUTTON = "//button[@id='add-to-cart-{}']"

    def add_product(self, slug: str):
        """Добавляет товар в корзину по его slug."""
        self.click((By.XPATH, self.ADD_BUTTON.format(slug)))

    def open_cart(self):
        self.click(self.CART_LINK)
