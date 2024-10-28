import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestCancelOrder:
    def test_cancel_order(self, browser):
        p = MarketPage(browser)
        p.add_to_cart()
        p.checkout()
        p.cancel_order()