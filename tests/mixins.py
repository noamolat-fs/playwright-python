from typing import Any

import pytest
from models.saucedemo import (
    SaucedemoCartPage,
    SaucedemoCheckoutPage,
    SaucedemoDashboardPage,
    SaucedemoInventoryPage,
    SaucedemoLoginPage,
)
from playwright.sync_api import Page, expect


class TestSaucedemoLoginMixin:
    login_username = "standard_user"
    login_password = "secret_sauce"

    def login(
        self,
        page: Page,
        username: str | None = None,
        password: str | None = None,
    ):
        loginpg = SaucedemoLoginPage(page, True)
        loginpg.login(
            username or self.login_username, password or self.login_password
        )

    def expect_logged_in(self, page: Page):
        invpg = SaucedemoDashboardPage(page)
        expect(invpg.logout_button).to_be_attached()


class TestSaucedemoLogoutMixin:
    def logout(self, page: Page):
        dashpg = SaucedemoDashboardPage(page)
        dashpg.logout()


class TestSaucedemoInventoryMixin:
    add_to_cart_items: list[str] = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
    ]

    def add_to_cart(self, page: Page, *items: str):
        invpg = SaucedemoInventoryPage(page, True)
        for item in items or self.add_to_cart_items:
            invpg.add_to_cart(item)


class TestSaucedemoCartMixin:
    expect_cart_items: list[str | tuple[str, int | None]] = [
        ("Sauce Labs Backpack", 1),
        ("Sauce Labs Bike Light", 1),
    ]

    def expect_cart(self, page: Page, *items: str | tuple[str, int | None]):
        cartpg = SaucedemoCartPage(page, True)
        for item in items or self.expect_cart_items:
            count: int | None = None
            if isinstance(item, tuple):
                item, count = item
            expect(cartpg.get_item(item, count)).to_have_count(1)


class TestSaucedemoCheckoutMixin:
    checkout_first_name = "Foo"
    checkout_last_name = "Bar"
    checkout_postal_code = 4102

    def checkout(
        self,
        page: Page,
        first_name: str | None = None,
        last_name: str | None = None,
        postal_code: int | None = None,
    ):
        checkpg = SaucedemoCheckoutPage(page, True)
        checkpg.checkout(
            first_name or self.checkout_last_name,
            last_name or self.checkout_last_name,
            postal_code or self.checkout_postal_code,
        )

    def expect_checked_out(self, page: Page):
        checkpg = SaucedemoCheckoutPage(page)
        expect(checkpg.complete_header).to_have_count(1)


class TestSaucedemoAuthenticatedMixin(
    TestSaucedemoLoginMixin, TestSaucedemoLogoutMixin
):
    @pytest.fixture(scope="function", autouse=True)
    def before_each_login(self, page: Page):
        self.login(page)
        yield

    @pytest.fixture(scope="function", autouse=True)
    def after_each_logout(self, page: Page):
        yield
        self.logout(page)


class TestSaucedemoFilledCartMixin(
    TestSaucedemoAuthenticatedMixin, TestSaucedemoInventoryMixin
):
    @pytest.fixture(scope="function", autouse=True)
    def before_each_add_to_cart(self, page: Page, before_each_login: Any):
        self.add_to_cart(page)
        yield
