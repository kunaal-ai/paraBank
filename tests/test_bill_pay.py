"""Testing bill payment for submission.
"""

from fixtures.fixtures import *


def test_submit_form_with_correct_values(
    user_login, payment_services_tab, bill_pay_page
):
    """Send valid inputs and submit form

    Args:
        user_login (fixture): log in user with correct credentials
        payment_services_tab (fixture): Instance of PaymentServicesTab class
        bill_pay_page (fixture): Instance of BillPay class
    """    
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
        "9786",
    )
