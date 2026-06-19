# Standard CSS Selector

page.locator("#name")  # using id
page.locator(".form-control")  # class
page.locator("input[type='text']")  #using tags and attributes

# XPath

page.locator("//button[@class='start']")  # attribute base xpath
page.locator("//button[text()='START']").click() # text-based xpath
page.locator("(//button[@class='start'])[1]") # index based xpath
page.locator("//h2[contains(text(),'Alerts &')]")  #contains based when the text or attribute value is length
