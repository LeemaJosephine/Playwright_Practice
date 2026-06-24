import os

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.set_default_timeout(25000)

    # enter content
    page.locator("#inputText").fill("Hello World")

    # Genrate the file
    page.locator("#generateTxt").click()

    # Wait for actual download
    with page.expect_download() as download_info:
        page.locator("#txtDownloadLink").click()

    download = download_info.value
    print(download.suggested_filename)
    folder_path = "C:\\Users\\leema\\OneDrive\\Desktop"
    download.save_as(os.path.join(folder_path, download.suggested_filename))
    # download.save_as(download.suggested_filename))  # point to the current folder
    browser.close()