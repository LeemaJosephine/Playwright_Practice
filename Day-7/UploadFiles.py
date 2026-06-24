from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.set_default_timeout(25000)

    page.locator("#singleFileInput").set_input_files("C:\\Users\\leema\\Downloads\\Playwright with Python Syllabus.pdf")
    page.get_by_text("Upload Single File").click()

    file_status= page.locator("#singleFileStatus").text_content()
    if "Playwright with Python Syllabus.pdf" in file_status:
        print("File Uploaded")
    else:
        print("File Not Uploaded")

    page.wait_for_timeout(10000)