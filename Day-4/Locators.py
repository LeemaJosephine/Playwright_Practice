from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://practicetestautomation.com/practice-test-login/")

    # GetByRole

    # page.get_by_role("heading", name="Test login").text_content()
    text = page.get_by_role("heading").first.text_content()
    print(text)

    # Get by label

    page.get_by_label("Username").fill("student")

    # CSS Selector
    # ID Locator
    page.locator("#password").fill("Password123")

    # # Name Locator
    # page.locator("input[name='password']").fill("testuser123")
    #
    # # XPath
    # page.locator("//input[@name='password']").fill("testuser123")

    page.get_by_text("Submit").nth(0).click()

    page.wait_for_timeout(5000)

    # Get by Placeholder
    page.get_by_placeholder("Username").fill("student")

