from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_shop(firefox_driver):
    # 1. Открываем сайт магазина
    login_page = LoginPage(firefox_driver)
    login_page.open()

    # 2. Авторизуемся как standard_user
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавляем в корзину три товара
    inventory_page = InventoryPage(firefox_driver)
    inventory_page.add_product("sauce-labs-backpack")
    inventory_page.add_product("sauce-labs-bolt-t-shirt")
    inventory_page.add_product("sauce-labs-onesie")

    # 4. Переходим в корзину
    inventory_page.open_cart()

    # 5. Нажимаем Checkout
    cart_page = CartPage(firefox_driver)
    cart_page.checkout()

    # 6. Заполняем форму данными
    checkout_page = CheckoutPage(firefox_driver)
    checkout_page.fill_customer_info(
        first_name="Кирилл",
        last_name="Гончаров",
        postal_code="457351",
    )

    # 7. Нажимаем Continue
    checkout_page.continue_to_overview()

    # 8. Читаем итоговую стоимость
    total_text = checkout_page.get_total_text()

    # 9. Проверяем сумму
    assert total_text == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', но получено: {total_text}"
    )
