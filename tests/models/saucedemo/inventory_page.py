from models.saucedemo.dashboard_page import DashboardPage


class InventoryPage(DashboardPage):
    path = "inventory.html"

    def add_to_cart(self, item: str):
        self.page.locator(f'[data-test="add-to-cart-{item}"]').click()
