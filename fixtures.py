from playwright.sync_api import Page
from pages.home_page import HomePage
import pytest


@pytest.fixture
def home_page(page: Page):
    home_page = HomePage(page)
    home_page.load()
    return home_page

@pytest.fixture
def user_login(page:Page):
    home_page = HomePage(page)
    home_page.load()
    home_page.user_log_in()