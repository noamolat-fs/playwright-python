import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def page_goto(page: Page):
    page.goto("https://playwright.dev/python/")
    yield  # the test will be run on this


def test_playwright_docs_title(page: Page):
    expect(page).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright Python"
    )


def test_playwright_docs_getstarted_heading(page: Page):
    get_started = page.locator("a.getStarted_Sjon")
    get_started.click()

    heading = page.locator("h1")

    expect(heading).to_have_text("Installation")
