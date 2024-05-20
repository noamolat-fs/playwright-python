from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def logout(self):
        self.page.get_by_role("button", name="Open Menu").click()
        self.page.locator('[data-test="logout-sidebar-link"]').click()

    def add_to_cart(self, item: str):
        self.page.locator(f'[data-test="add-to-cart-{item}"]').click()

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()

    def is_on_cart(self, item: str):
        expect(
            self.page.locator('[data-test="inventory-item-name"]')
        ).to_contain_text(item)
        expect(
            self.page.locator('[data-test="item-quantity"]')
        ).to_contain_text("1")

    def checkout(self, first_name: str, last_name: str, postal_code: int):
        self.page.locator('[data-test="checkout"]').click()
        self.page.locator('[data-test="firstName"]').click()
        self.page.locator('[data-test="firstName"]').fill(first_name)
        self.page.locator('[data-test="firstName"]').press("Tab")
        self.page.locator('[data-test="lastName"]').fill(last_name)
        self.page.locator('[data-test="lastName"]').press("Tab")
        self.page.locator('[data-test="postalCode"]').fill(f"{postal_code}")
        self.page.locator('[data-test="continue"]').click()
        self.page.locator('[data-test="finish"]').click()

    def is_order_successful(self):
        expect(
            self.page.locator('[data-test="complete-header"]')
        ).to_contain_text("Thank you for your order!")
