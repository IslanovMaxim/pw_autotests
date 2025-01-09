class Basket:
    #IN_CART = "//span[text()='1']"
    #CHOOSE_APT = "//div[text()='Сегодня - 1']"
    #CONFIRM_CHOOSE_BUTTON = "//button[text()='Выбрать аптеку']"
    # LAST_NAME = "[data-test='lastName']"
    # ZIP = "[data-test='postalCode']"
    # CNT_BTN = "[data-test='continue']"
    # FINISH_BTN = "[data-test='finish']"
    FINAL_TEXT = "//h1[text()='Спасибо, заказ оформлен!']"
    FINAL_TEXT_LESS_50 = "//h4[text()='Минимальная сумма заказа 50 ₽']"
    DECREASE_BTN = "[class='counter__button counter__button_dec']"
    INCREASE_BTN = "[class='counter__button counter__button_inc']"
    PRODUCT_COUNTER = "[class='counter__value j-counter-value']"
    DELETE_BTN = "[class='product-card__close j-product-card-close']"
    TOTAL_PRICE = '[class="price price_new j-total-price"]'
    TOTAL_DISCOUNT = '[class="f_discount j-total-discount"]'
    OLD_PRICE = '[class="price-search__content"]'
