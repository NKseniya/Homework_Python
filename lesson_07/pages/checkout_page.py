from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_customer_info(self, first_name: str, last_name: str,
                           postal_code: str):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def continue_to_overview(self):
        self.click(self.CONTINUE_BUTTON)

    def get_total_text(self) -> str:
        return self.find(self.TOTAL_LABEL).text
