from playwright.sync_api import Page


def test_selectors(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.pause()

    username = page.locator('[data-test="username"]')
    username.fill("standard_user")

    password = page.locator('//*[@id="password"]')
    password.fill("secret_sauce")

    login = page.get_by_text("Login")
    login.click()
