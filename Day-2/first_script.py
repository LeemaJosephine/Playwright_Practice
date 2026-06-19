from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Launch the browser
    # browser = p.chromium.launch(headless=False)
    browser = p.firefox.launch(headless=False)

    # Open a new page in the browser
    page = browser.new_page()

    # Load the URL
    page.goto("https://www.amazon.in/")

    # Add wait manually
    page.wait_for_timeout(3000)

    # browser version
    print(browser.version)

    # Close the browser
    browser.close()
