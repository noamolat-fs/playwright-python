from playwright.sync_api import Page

from models.saucedemo.page import Page as SaucedemoPage


class LoginPage(SaucedemoPage):
    path = ""

    def __init__(self, page: Page, goto=False):
        super().__init__(page, goto)
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
