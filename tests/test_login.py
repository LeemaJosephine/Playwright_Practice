from playwright.sync_api import sync_playwright, expect

def test_login(page):
        page.locator("#login2").click()
        page.locator("#loginusername").fill("testuser123")
        page.locator("#loginpassword").fill("testuser123")
        page.get_by_role("button", name="Log in").click()
        welcome_locator = page.locator("#nameofuser")
        expect(welcome_locator).to_contain_text("testuser123")

def test_invalid_login(page):
        page.locator("#login2").click()
        page.locator("#loginusername").fill("testuser")
        page.locator("#loginpassword").fill("testuser")
        page.get_by_role("button", name="Log in").click()
        welcome_locator = page.locator("#nameofuser")
        expect(welcome_locator).to_contain_text("testuser123")