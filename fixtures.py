from playwright.sync_api import Page
from pages.home_page import HomePage
import pytest


@pytest.fixture
def home_page(page: Page):
    home_page = HomePage(page)
    return home_page