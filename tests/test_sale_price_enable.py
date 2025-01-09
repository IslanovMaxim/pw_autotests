import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestSalePriceEnable:
    def test_sale_price_enable(self, browser):
        p = MarketPage(browser)
        p.sale_price_enable()

