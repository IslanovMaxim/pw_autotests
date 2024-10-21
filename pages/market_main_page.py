from pages.base import Base
from Locators.basket_page import Basket
from Locators.market_page import Market
from data.assertions import Assertions
from playwright.sync_api import Page
from data.constants import Constants
from Locators.auth import Auth


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def add_to_cart(self):                         #для товаров с ценой больше 50
        self.open("")
        self.click_element_by_index(Market.CITY_YES,1)
        self.input_value_by_index(Market.DRUG_INPUT, 0, Constants.drug_name)
        self.click(Market.CHOOSE_FROM_LIST)
        self.click_element_by_index(Market.ADD_BTN, 0)
        self.timeout(3000)
        self.click_text_by_index('₽', 0)

    def checkout(self):                              #для товаров с ценой больше 50
        #self.timeout(3000)
        #self.click(Basket.TO_SALE)
        #self.timeout(3000)
        self.click_by_text('Оформить заказ')
        self.input(Market.NUM_INPUT, Constants.login)
        self.click(Auth.APPROVE_NUM)
        self.timeout(3000)
        self.input(Auth.CODE_INPUT, Constants.code)
        self.click_text_by_index('Выбрать',0)
        self.click_text_by_index('Сегодня',2)
        #self.timeout(3000)
        self.click_text_by_index('Выбрать аптеку',1)
        self.timeout(3000)
        self.click_by_text('Оформить заказ')
        self.timeout(10000)
        # self.input(Basket.FIRST_NAME, "Ivan")
        # self.input(Basket.LAST_NAME, "Ivanov")
        # self.input(Basket.ZIP, "123456")
        # self.click(Basket.CNT_BTN)
        # self.click(Basket.FINISH_BTN)
        self.assertions.have_text(Basket.FINAL_TEXT, 'Спасибо, заказ оформлен!', "no")

    def add_to_cart_less_50(self):
        self.open("")
        self.click_element_by_index(Market.CITY_YES, 1)
        self.input_value_by_index(Market.DRUG_INPUT, 0, Constants.drug_name_less_50)
        self.click_text_by_index('Гематоген',0)
        self.click_element_by_index(Market.ADD_BTN, 0)
        self.timeout(3000)
        self.click_text_by_index('₽', 0)

    def checkout_less_50(self):
        self.assertions.contain_text("body > div.layout.j-layout > div.layout__main.j-layout-main > div.layout__body > div.page.page-cart.j-page-cart.j-page > div > div > div.box__row.page-cart__content.j-page-cart-content > div.box__col.box__col_md_4.page-cart__order > div > div > div.page-cart__details.j-total-details > div.cart-notify.j-cart-notify.page-cart__details-notify > h4",  'Минимальная сумма заказа 50 ₽', 'no')

    def checkout_choose_city(self):
        self.open("")
        self.click_text_by_index('Нет', 1)
        self.click_element_by_index(Market.CHOOSE_CITY_FROM_LIST, 0)
        self.timeout(3000)
        self.assertions.have_text('#anchor-header > div.header__inner > div.header__container.j-header-container > div.header__location.hidden_xs.d_md_f > div > div > a:nth-child(1)', 'Казань', "no")