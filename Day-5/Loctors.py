from tkinter.font import names

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    page.goto("https://ammazon.in")

    # GetByRole - Search box
    element = page.get_by_role('searchbox')
    element.fill("Mobile")
    # element.press("Enter")

    page.get_by_role("button", name="Go").nth(0).click()

    # GetByText
    page.get_by_text("Sell", exact=True).click()

    # Partial match
    page.get_by_text("Bestsell", exact=False).click()

    # GetByAltText

    # capture element
    page.get_by_alt_text("PD26_Event" ,exact=True).screenshot(path="Day-5/PD26_Event.png")
    page.get_by_alt_text("PD26_Event", exact=True).click()

    # Capture Visible screen
    page.screenshot(path="Day-5/Loctors.png")

    #Capture full screen
    page.screenshot(path="Day-5/LoctorsFullPage.png", full_page=True)

    page.wait_for_timeout(5000)

    context.tracing.stop(path="AmazonHeadlesstrace.zip")