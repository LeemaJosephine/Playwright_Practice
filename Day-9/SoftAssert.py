from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.set_default_timeout(25000)

    # Validate title
    expect(page).to_have_title("Automation Testing Practice")
    print("Title Verified: ", page.title())

    # Validate the url
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/")
    print("URL Verified: ", page.url)

    # Validate CheckBox
    page.locator("#monday").check()
    expect(page.locator("#monday")).to_be_checked()


