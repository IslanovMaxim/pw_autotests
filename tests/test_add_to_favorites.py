import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestIncreaseProduct:
    def test_increase_product(self, browser):
        p = MarketPage(browser)
        p.log_in()
        p.add_to_favorites()
