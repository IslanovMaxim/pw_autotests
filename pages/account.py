from Locators.account_page import Account
from pages.base import Base
from Locators.basket_page import Basket
from Locators.market_page import Market
from data.assertions import Assertions
from playwright.sync_api import Page
from data.constants import Constants
from Locators.auth import Auth


class AccountPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def orders_history_enable(self):
        self.click(Market.TO_PROFILE)
        self.click_by_text(Account.ORDERS)
        self.click_by_text(Account.ORDERS_HISTORY)
        self.assertions.have_text_first(Account.ORDER, '79000000000', 'no')
