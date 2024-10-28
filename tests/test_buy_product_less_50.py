import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestBuyProductLess50:
    def test_buy_product_less_50(self, browser):
        p = MarketPage(browser)
        p.add_to_cart_less_50()
        p.checkout_less_50()