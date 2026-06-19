from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.get_by_label("username").fill("username")
    page.get_by_label("password").fill("password")

    page.wait_for_timeout(5000)

