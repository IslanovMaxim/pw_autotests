import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestBuySetDiscountOnSecond:
    def test_buy_set_discount_on_second(self, browser):
        p = MarketPage(browser)
        #p.add_to_cart()
        p.buy_set_discount_on_second()