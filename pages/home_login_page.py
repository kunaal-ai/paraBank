"""Home Page 
"""
import os
from playwright.sync_api import Page


class HomePage:
    """Page objects and methods Home Page only"""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.user_name_text = page.locator("input[name=\"username\"]")
        self.password_text = page.locator("input[name=\"password\"]")
        self.log_in_button = page.locator("input.button")
        self.forget_login_button = page.locator(
            "#loginPanel > p:nth-child(2) > a:nth-child(1)"
        )

    def load(self: any):
        """Navigate to page given as base-url in pytest.ini"""
        self.page.goto("/")

    def user_log_in(self):
        username = os.environ.get("ui_USER1_USERNAME")
        password = os.environ.get("ui_USER1_PASSWORD")
        
        self.user_name_text.fill(username)
        self.password_text.fill(password)
        self.log_in_button.click()

    def forget_login(self):
        self.forget_login_button.click()
