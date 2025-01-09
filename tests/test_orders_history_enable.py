import pytest

from pages.account import AccountPage
from pages.market_main_page import MarketPage


@pytest.mark.regression
#@pytest.mark.usefixtures('user_login')
class TestOrdersHistoryEnable:
    def test_orders_history_enable(self, browser):
        p = MarketPage(browser)
        a = AccountPage(browser)
        p.log_in()
        a.orders_history_enable()


