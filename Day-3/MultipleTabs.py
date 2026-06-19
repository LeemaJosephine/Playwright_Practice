from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page1 = browser.new_page()
    page2 = browser.new_page()

    page1.goto("https://google.com")
    page2.goto("https://amazon.in")

    page1.wait_for_timeout(2000)
    page2.wait_for_timeout(2000)
