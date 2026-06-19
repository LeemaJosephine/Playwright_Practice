from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # Launches chrome browser and it will be visible
    # page  = browser.new_page()  # open the new tab
    # page.goto("https://amazon.in") # navigate to url
    # page.wait_for_timeout(3000)
    # browser.close()

    # Browser Context
    context1 = browser.new_context()  # Different Windows
    context2 = browser.new_context()

    page1 = context1.new_page()  # Represents the tab
    page2 = context2.new_page()

    page1.goto("https://google.com")
    page2.goto("https://amazon.in")

    page1.wait_for_timeout(3000)
    page2.wait_for_timeout(3000)

    browser.close()
