from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.set_default_timeout(25000)

    # GetByPlaceHolder

    page.get_by_placeholder("Enter Name").fill("testuser")  # testuser
    page.get_by_placeholder("Enter Name").type("123",delay=1000) # testuser123
    page.get_by_placeholder("Enter Name").fill("Hello") # Hello

    page.get_by_placeholder("Enter Email").fill("testuser@gmail.com")
    # page.get_by_label("Name").fill("testuser")
    #page.get_by_label("Email").fill("testuser@gmail.com")

    # Normal click
    page.get_by_role("button", name="start").click()

    page.wait_for_timeout(2000)

    # double click
    page.get_by_role("button", name="Copy Text").dblclick()
    #
    page.wait_for_timeout(2000)
    #
    # right click
    page.get_by_role("button", name="Copy Text").click(button="right")
    #
    page.wait_for_timeout(2000)
    # force click
    # page.get_by_role("button", name="start").click(force=True)

    # Press - Keyboard actions
    search = page.locator("#Wikipedia1_wikipedia-search-input")
    search.fill("Playwright")
    search.press("Control+A")
    search.press("Enter")
    #
    # Clear
    page.get_by_placeholder("Enter Name").clear()
    page.get_by_placeholder("Enter Email").fill("")

    # DropDown

    # select by value
    page.locator("#country").select_option("france")

    page.wait_for_timeout(2000)

    # select by label
    page.locator("#country").select_option(label="         Canada       ")

    page.wait_for_timeout(2000)

    # select by index
    page.locator("#country").select_option(index=9)

    # Radio button

    gender = page.get_by_label("Female")
    gender.check()
    print(gender.is_checked())

    # CheckBox
    days = page.get_by_label("Monday")
    days.check()
    print(days.is_checked())

    day2 = page.get_by_label("Tuesday")
    day2.check()
    print(day2.is_checked())

    day2.uncheck()
    print(day2.is_checked())

    # Waits
    page.goto("https://www.hyrtutorials.com/p/waits-demo.html")

    page.locator("#btn1").click()

    page.get_by_placeholder("Textbox1").nth(0).wait_for(state="visible")
    page.get_by_placeholder("Textbox1").nth(0).fill("Hello")

    page.wait_for_timeout(5000)