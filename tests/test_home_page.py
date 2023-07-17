"""Tests for Home Page
"""
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from fixtures import *


def test_user_log_in_sucessfully(home_page, page: Page):
    """Verify if user is landed on its page after entering correct credentials

    Args:
        home_page (_type_): class HomePage object
        page (Page): page object
    """

    
    home_page.user_log_in()
    expect(page).to_have_url("/parabank/overview.htm")


def test_forget_login(home_page, page: Page):
    """click on forget login and verify page

    Args:
        home_page (_type_): fixture, class HomePage object
        page (Page): page object
    """
    home_page.forget_login()
    expect(page).to_have_url("/parabank/lookup.htm")
