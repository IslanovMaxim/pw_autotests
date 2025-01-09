import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestAddToFavorites:
    def test_add_to_favorites(self, browser):
        p = MarketPage(browser)
        p.log_in()
        p.add_to_favorites()
