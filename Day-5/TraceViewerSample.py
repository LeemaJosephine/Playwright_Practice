from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Start Trace
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page=context.new_page()
    page.goto("https://google.com/")

    search = page.get_by_role("combobox", name="Search")
    search.fill("Playwright")
    page.keyboard.press("Enter")

    #Strop Trace
    context.tracing.stop(path="trace.zip")

    browser.close()
