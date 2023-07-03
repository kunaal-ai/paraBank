import re
from playwright.sync_api import Page, expect
from pages.homePage import HomePage

def test_user_at_home_page(page: Page):
    
    hp = HomePage(page)
    hp.load()

    expect(page).to_have_title(re.compile("ParaBank"))

    register = page.get_by_role("link", name="Register")

    # expect(register).to_have_attribute("href", "register.htm")

    # register.click()

    # expect(page).to_have_url(re.compile(".*register"))