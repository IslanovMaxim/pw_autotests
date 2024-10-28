import pytest
from pages.auth_page import Main
from pages.market_main_page import MarketPage


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        m = Main(browser)
        m.user_login()
        p = MarketPage(browser)
        p.to_favorites()