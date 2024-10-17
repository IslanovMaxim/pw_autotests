from asyncio import timeout

from pages.base import Base
from data.constants import Constants
from Locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page

class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("lk/login")
        self.click(Auth.CITY_YES)
        self.input(Auth.PHONE_INPUT, Constants.login)
        self.click(Auth.APPROVE_NUM)
        self.timeout(3000)
        self.input(Auth.CODE_INPUT, Constants.code)
        self.assertion.check_URL('', "Wrong URL")