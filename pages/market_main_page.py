from pages.base import Base
from Locators.basket_page import Basket
from Locators.market_page import Market
from data.assertions import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def add_to_cart(self):
        #self.click(Market.CITY_YES)
        self.input_value_by_index(Market.DRUG_INPUT, 0, 'Пенталгин')
        self.click(Market.CHOOSE_FROM_LIST)

    def checkout(self):
        self.click_element_by_index(Basket.ADD_BTN, 0)
        self.timeout(3000)
        self.click_by_index_text('₽',0)
        #self.timeout(3000)
        #self.click(Basket.TO_SALE)
        #self.timeout(3000)
        self.click_by_text('Оформить заказ')
        self.click_by_index_text('Выбрать',0)
        self.click_by_index_text('Сегодня',2)
        self.timeout(3000)
        # self.input(Basket.FIRST_NAME, "Ivan")
        # self.input(Basket.LAST_NAME, "Ivanov")
        # self.input(Basket.ZIP, "123456")
        # self.click(Basket.CNT_BTN)
        # self.click(Basket.FINISH_BTN)
        # self.assertions.have_text(Basket.FINAL_TEXT, "Checkout: Complete!", "no")