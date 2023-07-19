from playwright.sync_api import Page
from fixtures.fixtures import *


def test_submit_form_with_correct_values(user_login, payment_services_tab, bill_pay_page, ):
    payment_services_tab.bill_pay_link.click()

    bill_pay_page.submit_form(
        "test",
        "address XYZ",
        "city CTY",
        "Ohio",
        "12345",
        "9998887766",
        "221144",
        "221144",
        "9786"
    )
