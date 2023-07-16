"""Tests for Home Page
"""
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_user_log_in_sucessfully(page: Page):
    """Verify if user is landed on its page after entering correct credentials

    Args:
        page (Page): page object
    """

    home_page = HomePage(page)
    home_page.load()
    home_page.user_log_in()
    expect(page).to_have_url("/parabank/overview.htm")
