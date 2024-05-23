from playwright.sync_api import Page

from models.saucedemo.page import Page as SaucedemoPage


class DashboardPage(SaucedemoPage):
    def __init__(self, page: Page, goto=False):
        super().__init__(page, goto)
        self.logout_button = page.locator('[data-test="logout-sidebar-link"]')
        self.cart = page.locator('[data-test="shopping-cart-link"]')

    def open_menu(self):
        self.page.get_by_role("button", name="Open Menu").click()

    def close_menu(self):
        self.page.get_by_role("button", name="Close Menu").click()

    def logout(self):
        self.open_menu()
        self.logout_button.click()
