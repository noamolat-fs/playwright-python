from urllib.parse import urljoin

from playwright.sync_api import Page


class BasePage:
    base_url: str
    path: str

    def __init__(self, page: Page, goto=False):
        self.page = page
        if goto:
            self.goto()

    def goto(self, path: str = ""):
        url = urljoin(self.base_url, self.path)
        if path:
            url = url.rstrip("/") + "/" + path.lstrip("/")
        return self.page.goto(url)
