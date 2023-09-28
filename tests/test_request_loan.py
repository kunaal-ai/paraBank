import pytest
from playwright.sync_api import Page, expect


def test_request_loan_amount_valid_inputs(
    home_page, payment_services_tab, request_loan_page
):
    home_page.load()
    home_page.user_log_in()
    payment_services_tab.request_loan_link.click()
    request_loan_page.loan_amount("5000")
    request_loan_page.down_payment("8000")
    # request_loan_page.apply_now()
