import pytest
from playwright.sync_api import Page, expect
from pages.overview_page import OverviewPage

@pytest.mark.smoke
def test_account_services_menu(home_page, payment_services_tab):
   
    home_page.load()
    home_page.user_log_in()
    payment_services_tab.open_new_account_link.click()
    payment_services_tab.accounts_overview_link.click()
    payment_services_tab.transfer_funds_link.click()
    payment_services_tab.bill_pay_link.click()
    payment_services_tab.find_tranactions_link.click()
    payment_services_tab.update_contact_info_link.click()
    payment_services_tab.request_loan_link.click()
    payment_services_tab.log_out_link.click()
