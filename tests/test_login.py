import pytest
from utils.excel_reader import read_excel, read_csv , read_json

test_data = read_excel("C:\\Users\\leema\\PycharmProjects\\Playwright_Practice\\Data\\TestData_Demo.xlsx","LoginData")
csv_data = read_csv("C:\\Users\\leema\\PycharmProjects\\Playwright_Practice\\Data\\Demo_TestData.csv")
json_data = read_json("C:\\Users\\leema\\PycharmProjects\\Playwright_Practice\\Data\\LoginData.json")

@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("users", json_data)
def test_validLogin(page, users):
        page.locator("#login2").click()
        page.locator("#loginusername").fill(users["username"])
        page.locator("#loginpassword").fill(users["password"])
        page.get_by_role("button", name="Log in").click()
        # welcome_locator = page.locator("#nameofuser")
        # expect(welcome_locator).to_contain_text("testuser123")

@pytest.mark.regression
@pytest.mark.parametrize("users", json_data)
def test_invalidlogin(page, users):
        page.locator("#login2").click()
        page.locator("#loginusername").fill(users["username"])
        page.locator("#loginpassword").fill(users["password"])
        page.get_by_role("button", name="Log in").click()
        # welcome_locator = page.locator("#nameofuser")
        # expect(welcome_locator).to_contain_text("testuser123")

@pytest.mark.sanity
@pytest.mark.parametrize("users", json_data)
def test_login(page, users):
        page.locator("#login2").click()
        page.locator("#loginusername").fill(users["username"])
        page.locator("#loginpassword").fill(users["password"])
        page.get_by_role("button", name="Log in").click()
        # welcome_locator = page.locator("#nameofuser")
        # expect(welcome_locator).to_contain_text("testuser123")
