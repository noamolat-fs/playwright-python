from playwright.sync_api import Page

from models.saucedemo.dashboard_page import DashboardPage


class CheckoutPage(DashboardPage):
    path = "checkout-step-one.html"

    def __init__(self, page: Page, goto=False):
        super().__init__(page, goto)
        self.first_name = self.page.locator('[data-test="firstName"]')
        self.last_name = self.page.locator('[data-test="lastName"]')
        self.postal_code = self.page.locator('[data-test="postalCode"]')
        self.continue_button = self.page.locator('[data-test="continue"]')
        self.finish_button = self.page.locator('[data-test="finish"]')
        self.complete_header = self.page.locator(
            '[data-test="complete-header"]'
        ).get_by_text("Thank you for your order!")

    def checkout(self, first_name: str, last_name: str, postal_code: int):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(f"{postal_code}")
        self.continue_button.click()
        self.finish_button.click()
