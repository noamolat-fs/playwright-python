from playwright.sync_api import Page

from models.saucedemo.dashboard_page import DashboardPage


class CartPage(DashboardPage):
    path = "cart.html"

    def __init__(self, page: Page, goto=False):
        super().__init__(page, goto)
        self.checkout_button = page.locator('[data-test="checkout"]')

    def checkout(self):
        self.checkout_button.click()

    def get_item(self, item: str, quantity: int | None = None):
        items = self.page.locator('[data-test="inventory-item"]')
        litem = items.filter(has_text=item)
        if quantity is not None:
            litem = litem.filter(
                has=self.page.locator(
                    '[data-test="item-quantity"]'
                ).get_by_text(f"{quantity}")
            )
        return litem
