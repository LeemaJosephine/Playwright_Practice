from playwright.sync_api import sync_playwright

def handle_alert(dialog):
    print("Alert text", dialog.message)
    print(dialog.type)

    if dialog.type == "alert":
        dialog.accept()

    elif dialog.type == "confirm":
        dialog.dismiss()   # or
        # dialog.accept()

    elif dialog.type == "prompt":
        dialog.accept("Leema")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    # Register to handel the alert
    page.on("dialog" ,handle_alert)


    page.goto("https://demo.automationtesting.in/Alerts.html")
    page.set_default_timeout(25000)

    #Alert
    page.locator("button.btn.btn-danger").click()

    #Confirm
    page.get_by_text("Alert with OK & Cancel ").click()
    page.locator("button.btn.btn-primary").click()

    text = page.locator("#demo").text_content()
    print(text)

    #Prompt
    page.get_by_text("Alert with Textbox ").click()
    page.locator("button.btn.btn-info").click()

    text = page.locator("#demo1").text_content()
    print(text)

    page.wait_for_timeout(3000)

