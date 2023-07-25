''' pass
'''
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.bill_pay import BillPay
from pages.helper_pom.payment_services_tab import PaymentServicesTab



@pytest.fixture
def home_page(page: Page):
    home_page = HomePage(page)
    home_page.load()
    return home_page


@pytest.fixture
def user_login(page: Page):
    home_page = HomePage(page)
    home_page.load()
    home_page.user_log_in()
    print("✅ User logged in using user_login fixture")


@pytest.fixture
def bill_pay_page(page: Page):
    bill_pay_page = BillPay(page)
    return bill_pay_page

@pytest.fixture
def payment_services_tab(page:Page):
    payment_services_tab = PaymentServicesTab(page)
    return payment_services_tab