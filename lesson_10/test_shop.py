import allure

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.title("Покупка товаров в интернет-магазине saucedemo.com")
@allure.description(
    "Авторизация под standard_user, добавление трёх товаров в корзину, "
    "оформление заказа и проверка итоговой суммы на странице Overview."
)
@allure.feature("Интернет-магазин saucedemo.com")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(firefox_driver):
    login_page = LoginPage(firefox_driver)

    with allure.step("Открыть сайт магазина"):
        login_page.open()

    with allure.step("Авторизоваться как standard_user"):
        login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(firefox_driver)

    with allure.step("Добавить в корзину Sauce Labs Backpack"):
        inventory_page.add_product("sauce-labs-backpack")

    with allure.step("Добавить в корзину Sauce Labs Bolt T-Shirt"):
        inventory_page.add_product("sauce-labs-bolt-t-shirt")

    with allure.step("Добавить в корзину Sauce Labs Onesie"):
        inventory_page.add_product("sauce-labs-onesie")

    with allure.step("Перейти в корзину"):
        inventory_page.open_cart()

    cart_page = CartPage(firefox_driver)

    with allure.step("Нажать кнопку Checkout"):
        cart_page.checkout()

    checkout_page = CheckoutPage(firefox_driver)

    with allure.step("Заполнить форму: имя, фамилия, почтовый индекс"):
        checkout_page.fill_customer_info(
            first_name="Кирилл",
            last_name="Гончаров",
            postal_code="457351",
        )

    with allure.step("Нажать кнопку Continue"):
        checkout_page.continue_to_overview()

    with allure.step("Прочитать итоговую стоимость (Total)"):
        total_text = checkout_page.get_total_text()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total_text == "Total: $58.29", (
            f"Ожидалось 'Total: $58.29', но получено: {total_text}"
        )
