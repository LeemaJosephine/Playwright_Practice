from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.set_default_timeout(25000)

    #Locate the table

    table = page.locator("#productTable")
    print("Table Found: ", table.is_visible())

    # Count the columns
    # //table[@id='productTable']//thead//th
    columns = page.locator("#productTable thead th").count()
    print("Columns Found: ", columns)

    # Count the rows
    # //table[@id='productTable']//tbody//tr
    rows = page.locator("#productTable tbody tr").count()
    print("Row Found: ", rows)

    # Count rows including the header
    # //table[@id='productTable']//tr
    rowCount = page.locator("#productTable tr").count()
    print("Row Count including header: ", rowCount)

    # Read Entire Table Data

    # Get the row count
    rows = page.locator("#productTable tr")
    row_count = rows.count()

    for i in range(rowCount):
        row_text = rows.nth(i).inner_text()
        print(row_text)

    # Read Specific cell Value - First product name
    # //table[@id='productTable']//tbody//tr[1]//td[2]
    value = page.locator("#productTable tbody tr:nth-child(1) td:nth-child(2)").inner_text()
    print("First Product name: " , value)


    # Select checkbox based on product name

    rows = page.locator("#productTable tbody tr")

    for i in range(rows.count()):
        product_name = rows.nth(i).locator("td").nth(1).inner_text()

        if product_name == "Tablet":
            rows.nth(i).locator("input[type='checkbox']").check()
            break

    page.wait_for_timeout(5000)
    browser.close()
