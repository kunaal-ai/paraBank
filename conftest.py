""" pass
"""
import pytest
from playwright.sync_api import Page
from pages.home_login_page import HomePage
from pages.bill_pay_page import BillPay
from pages.helper_pom.payment_services_tab import PaymentServicesTab

@pytest.fixture
def home_page(page: Page):
    return HomePage(page)


# @pytest.fixture
# def user_login(page: Page):
#     return HomePage(page)


@pytest.fixture
def bill_pay_page(page: Page):
    return BillPay(page)

@pytest.fixture
def payment_services_tab(page: Page):
    return PaymentServicesTab(page)