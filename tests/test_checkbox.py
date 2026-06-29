from playwright.sync_api import sync_playwright

def test_checkbox():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.set_default_timeout(25000)

        # Validate title
        assert page.title()  == "Automation Testing Practice"
        print("Title Verified: ", page.title())

        # Validate the url
        assert "blogspot" in page.url
        print("URL Verified: ", page.url)

        # Validate CheckBox
        page.locator("#monday").check()

        assert page.locator("#monday").is_checked()