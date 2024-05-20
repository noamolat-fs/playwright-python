import pytest
from models.dashboard_page import DashboardPage
from models.login_page import LoginPage
from playwright.sync_api import Page, expect


class TestExample:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")
        yield

    @pytest.fixture(scope="function", autouse=True)
    def after_each(self, page: Page):
        yield
        dashboard_page = DashboardPage(page)
        dashboard_page.logout()

    @pytest.mark.fast
    def test_add_to_cart(self, page: Page):
        dashboard_page = DashboardPage(page)
        dashboard_page.add_to_cart("sauce-labs-backpack")
        dashboard_page.open_cart()
        dashboard_page.is_on_cart("Sauce Labs Backpack")

    # @pytest.mark.xfail(reason="work-in-progress", run=False)
    def test_checkout(self, page: Page):
        dashboard_page = DashboardPage(page)
        dashboard_page.add_to_cart("sauce-labs-backpack")
        dashboard_page.open_cart()
        dashboard_page.checkout("First Name", "Last Name", 4102)
        dashboard_page.is_order_successful()


@pytest.mark.skip(reason="deprecated")
class TestExample1:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto("https://www.saucedemo.com/")
        page.locator('[data-test="username"]').click()
        page.locator('[data-test="username"]').fill("standard_user")
        page.locator('[data-test="password"]').click()
        page.locator('[data-test="password"]').fill("secret_sauce")
        page.locator('[data-test="login-button"]').click()
        yield

    @pytest.fixture(scope="function", autouse=True)
    def after_each(self, page: Page):
        yield
        page.get_by_role("button", name="Open Menu").click()
        page.locator('[data-test="logout-sidebar-link"]').click()

    def test_add_to_cart(self, page: Page):
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.locator('[data-test="shopping-cart-link"]').click()
        expect(
            page.locator('[data-test="inventory-item-name"]')
        ).to_contain_text("Sauce Labs Backpack")
        expect(page.locator('[data-test="item-quantity"]')).to_contain_text(
            "1"
        )

    def test_checkout(self, page: Page):
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.locator('[data-test="shopping-cart-link"]').click()
        expect(
            page.locator('[data-test="inventory-item-name"]')
        ).to_contain_text("Sauce Labs Backpack")
        expect(page.locator('[data-test="item-quantity"]')).to_contain_text(
            "1"
        )
        page.locator('[data-test="checkout"]').click()
        page.locator('[data-test="firstName"]').click()
        page.locator('[data-test="firstName"]').fill("First Name")
        page.locator('[data-test="firstName"]').press("Tab")
        page.locator('[data-test="lastName"]').fill("Last Name")
        page.locator('[data-test="lastName"]').press("Tab")
        page.locator('[data-test="postalCode"]').fill("4102")
        page.locator('[data-test="continue"]').click()
        page.locator('[data-test="finish"]').click()
        expect(page.locator('[data-test="complete-header"]')).to_contain_text(
            "Thank you for your order!"
        )
