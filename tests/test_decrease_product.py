import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestDecreaseProduct:
    def test_decrease_product(self, browser):
        p = MarketPage(browser)
        p.add_to_cart()
        p.decrease_product()