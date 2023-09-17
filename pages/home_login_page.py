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
        try:
            PASSWORD = os.environ['PASSWORD']
        except KeyError:
            import utils.secret_config
            PASSWORD = utils.secret_config.PASSWORD

        self.user_name_text.fill("john")
        self.password_text.fill(PASSWORD)
        self.log_in_button.click()

    def forget_login(self):
        self.forget_login_button.click()
