import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestLogOut:
    def test_log_out(self, browser):
        p = MarketPage(browser)
        p.log_in()
