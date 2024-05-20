from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def username(self):
        return self.page.locator('[data-test="username"]')

    @property
    def password(self):
        return self.page.locator('[data-test="password"]')

    @property
    def login_btn(self):
        return self.page.locator('[data-test="login-button"]')

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
