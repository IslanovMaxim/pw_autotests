import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestChooseCity:
    def test_choose_city(self, browser):
        p = MarketPage(browser)
        #p.add_to_cart_less_50()
        p.checkout_choose_city()