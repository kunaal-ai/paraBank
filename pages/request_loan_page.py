"""Loan request page
"""
from playwright.sync_api import Page


class RequestLoanPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.loan_amount_text = page.locator("input[id='amount']")
        self.down_payment_text = page.locator("input[id='downPayment']")
        # self.from_account = page.locator("")
        self.button_apply_now = page.locator("input.button")

    def loan_amount(self, amount: str):
        self.loan_amount_text.fill(amount)

    def down_payment(self, amount: str):
        self.down_payment_text.fill(amount)

    def apply_now(self):
        self.button_apply_now.click()
