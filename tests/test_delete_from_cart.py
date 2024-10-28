import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestDeleteFromCart:
    def test_delete_from_cart(self, browser):
        p = MarketPage(browser)
        p.add_to_cart()
        p.delete_from_cart()