from Locators.account_page import Account
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
        self.assertions.have_text_last(Basket.FINAL_TEXT_LESS_50,  'Минимальная сумма заказа 50 ₽', 'no')

    def checkout_choose_city(self):
        self.open("")
        self.click_text_by_index('Нет', 1)
        self.click_element_by_index(Market.CHOOSE_CITY_FROM_LIST, 0)
        self.timeout(3000)
        self.assertions.have_text_first(Market.CHANGED_CITY, 'Казань', "no")

    def decrease_product(self):
        self.click_element_by_index(Basket.INCREASE_BTN, 0)
        self.click_element_by_index(Basket.DECREASE_BTN, 0)

        self.assertions.have_text_first(Basket.PRODUCT_COUNTER, '1', "no")

    def increase_product(self):
        self.click_element_by_index(Basket.INCREASE_BTN, 0)
        self.assertions.have_text_first(Basket.PRODUCT_COUNTER, '2', "no")

    def delete_from_cart(self):
        self.click(Basket.DELETE_BTN)
        self.click(Market.CONFIRM_DELETE_FROM_CART)
        self.assertions.have_text(Market.EMPTY_CART, 'Корзина пуста', "no")

    def to_favorites(self):
        self.click(Market.TO_FAVORITES)
        self.timeout(3000)
        self.assertions.check_url('lk?lk=favorite', "Wrong URL")

    def buy_set_2_1(self):
        self.open("")
        self.click_element_by_index(Market.CITY_YES, 1)
        self.input_value_by_index(Market.DRUG_INPUT, 0, Constants.drug_name_set_2_1)
        self.click_text_by_index('Гематоген',0)
        self.click_element_by_index(Market.ADD_BTN, 0)
        self.click_element_by_index(Basket.INCREASE_BTN, 0)
        self.click_element_by_index(Basket.INCREASE_BTN, 0)
        self.timeout(3000)
        self.click_text_by_index('₽', 0)
        self.assertions.have_text(Basket.TOTAL_PRICE, '81 ₽', "no")
        self.assertions.have_text(Basket.TOTAL_DISCOUNT, '-39 ₽', "no")


    def buy_set_discount_on_second(self):
        self.open("")
        self.click_element_by_index(Market.CITY_YES, 1)
        self.input_value_by_index(Market.DRUG_INPUT, 0, Constants.drug_name_set_discount_on_second)
        self.click_text_by_index('Канефрон',0)
        self.click_element_by_index(Market.ADD_BTN, 0)
        self.click_element_by_index(Basket.INCREASE_BTN, 0)
        self.timeout(3000)
        self.click_text_by_index('₽', 0)
        self.assertions.have_text(Basket.TOTAL_PRICE, '1 298 ₽', "no")
        self.assertions.have_text(Basket.TOTAL_DISCOUNT, '-200 ₽', "no")

    def cancel_order(self):
        self.click(Market.TO_PROFILE)
        self.click_element_by_index(Account.TO_ORDER, 0)
        self.click(Account.CANCEL_BTN)
        self.assertions.have_text(Account.EMPTY_ORDERS, 'Ваш заказ отменен', "no")
        self.screenshot(path="pw_autotests/screenshots/cancel_order.png")