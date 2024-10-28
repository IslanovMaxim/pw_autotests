import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestBuySet2Plus1:
    def test_buy_set_2_1(self, browser):
        p = MarketPage(browser)
        #p.add_to_cart()
        p.buy_set_discount_on_second()