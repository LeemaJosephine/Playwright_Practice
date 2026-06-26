from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("http://demoblaze.com/index.html")
    page.set_default_timeout(25000)

    page.locator("#login2").click()
    page.locator("#loginusername").fill("testuser123")
    page.locator("#loginpassword").fill("testuser123")
    page.get_by_role("button", name="Log in").click()

    # Locate the element
    welcome_locator = page.locator("#nameofuser")
    # # Wait for element to be visible
    # welcome_locator.wait_for(state="visible")
    # # Get the text content
    # welcome_message = welcome_locator.text_content()
    # print(welcome_message)

    # Hard Assertion
    # assert "testuser123" in welcome_message

    # soft assertion
    expect(welcome_locator).to_contain_text("testuser123")


