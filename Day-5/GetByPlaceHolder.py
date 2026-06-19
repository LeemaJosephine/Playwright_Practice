from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    # GetByPlaceHolder

    page.get_by_placeholder("Enter Name").fill("testuser")
    page.get_by_placeholder("Enter Email").fill("testuser@gmail.com")
    # page.get_by_label("Name").fill("testuser")
    #page.get_by_label("Email").fill("testuser@gmail.com")

    page.wait_for_timeout(5000)