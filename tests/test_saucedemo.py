from mixins import (
    TestSaucedemoAuthenticatedMixin,
    TestSaucedemoCartMixin,
    TestSaucedemoCheckoutMixin,
    TestSaucedemoFilledCartMixin,
    TestSaucedemoInventoryMixin,
    TestSaucedemoLoginMixin,
)
from playwright.sync_api import Page


class TestSaucedemoLogin(TestSaucedemoLoginMixin):
    def test_login(self, page: Page):
        self.login(page)
        self.expect_logged_in(page)


class TestSaucedemoInventory(
    TestSaucedemoAuthenticatedMixin,
    TestSaucedemoInventoryMixin,
    TestSaucedemoCartMixin,
):
    def test_add_to_cart(self, page: Page):
        self.add_to_cart(page)
        self.expect_cart(page)


class TestSaucedemoCheckout(
    TestSaucedemoFilledCartMixin, TestSaucedemoCheckoutMixin
):
    def test_checkout(self, page: Page):
        self.checkout(page)
        self.expect_checked_out(page)
