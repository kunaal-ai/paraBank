import pytest
import re
from playwright.sync_api import Page, expect


@pytest.mark.smoke
# def test_account_services_menu(user_login, payment_services_tab):
#     payment_services_tab.open_new_account_link.click()
#     payment_services_tab.accounts_overview_link.click()
#     payment_services_tab.transfer_funds_link.click()
#     payment_services_tab.bill_pay_link.click()
#     payment_services_tab.find_tranactions_link.click()
#     payment_services_tab.update_contact_info_link.click()
#     payment_services_tab.request_loan_link.click()
#     payment_services_tab.log_out_link.click()


# @pytest.mark.regression
def test_open_new_account(user_login, payment_services_tab, page: Page):
    payment_services_tab.open_new_account_link.click()
    expect(page).to_have_url("/parabank/openaccount.htm")


# @pytest.mark.regression
def test_accounts_overview(user_login, payment_services_tab, page: Page):
    payment_services_tab.accounts_overview_link.click()
    expect(page).to_have_url("/parabank/overview.htm")


# @pytest.mark.regression
def test_trasnfer_funds(user_login, payment_services_tab, page: Page):
    payment_services_tab.transfer_funds_link.click()
    expect(page).to_have_url("/parabank/transfer.htm")


# @pytest.mark.regression
def test_bill_pay(user_login, payment_services_tab, page: Page):
    payment_services_tab.bill_pay_link.click()
    expect(page).to_have_url("/parabank/billpay.htm")


# @pytest.mark.regression
def test_find_tranactions(user_login, payment_services_tab, page: Page):
    payment_services_tab.find_tranactions_link.click()
    expect(page).to_have_url("/parabank/findtrans.htm")


# @pytest.mark.regression
def test_update_contact_info(user_login, payment_services_tab, page: Page):
    payment_services_tab.update_contact_info_link.click()
    expect(page).to_have_url("/parabank/updateprofile.htm")


# @pytest.mark.regression
def test_request_loan(user_login, payment_services_tab, page: Page):
    payment_services_tab.request_loan_link.click()
    expect(page).to_have_url("/parabank/requestloan.htm")


# @pytest.mark.regression
def test_log_out(user_login, payment_services_tab, page: Page):
    payment_services_tab.log_out_link.click()
    expect(page).to_have_url(re.compile(".*index.*"))

