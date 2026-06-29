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