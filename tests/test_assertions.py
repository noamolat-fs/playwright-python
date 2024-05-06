from playwright.sync_api import Page, expect


def test_assertions(page: Page):
    page.goto("https://kitchen.applitools.com/")
    # page.pause()

    h1 = page.get_by_text("The Kitchen")

    expect(h1).to_have_count(1)
    # expect(h1).not_to_have_count(1)

    expect(h1).to_be_visible()
    # expect(h1).to_be_hidden()

    selecta = page.get_by_role("link", name="Select")
    selecta.click()

    select = page.get_by_label("Single Select")

    expect(select).to_be_enabled()
    # expect(select).to_be_disabled()

    h1 = page.locator("h1")

    expect(h1).to_have_text("Select")
    # expect(h1).not_to_have_text("Select")

    expect(select).to_have_attribute("name", "spices-select-single")
    # expect(select).not_to_have_attribute("name", "spices-select-single")

    expect(page).to_have_title("Select | The Kitchen")
    # expect(page).not_to_have_title("Select | The Kitchen")

    expect(page).to_have_url(
        "https://kitchen.applitools.com/ingredients/select"
    )
    # expect(page).not_to_have_url("https://kitchen.applitools.com/ingredients/select")
