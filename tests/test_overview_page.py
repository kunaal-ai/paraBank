from playwright.sync_api import Page, expect
from pages.overview_page import OverviewPage
from fixtures import *

def test_account_services_menu(user_login, page: Page):
    over_view_page = OverviewPage(page)
    over_view_page.open_new_account_link.click()
    over_view_page.accounts_overview_link.click()
    over_view_page.transfer_funds_link.click()
    over_view_page.bill_pay_link.click()
    over_view_page.find_tranactions_link.click()
    over_view_page.update_contact_info_link.click()
    over_view_page.request_loan_link.click()
    over_view_page.log_out_link.click()
    