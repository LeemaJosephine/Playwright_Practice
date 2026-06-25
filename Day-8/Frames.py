from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://demo.automationtesting.in/Frames.html")
    page.set_default_timeout(25000)

    # Iframe using variable
    frame = page.frame_locator("#singleframe")  #id
    frame.locator("input[type='text']").fill("Hello World")

    page.get_by_text("Iframe with in an Iframe").click()

    outer_frame = page.frame_locator("iframe[src='MultipleFrames.html']")
    inner_frame = outer_frame.frame_locator("iframe")  # from parent to child frame

    inner_frame.locator("input[type='text']").fill("Hello World")
    text = outer_frame.locator("h5").text_content()
    print(text)

    page.wait_for_timeout(5000)