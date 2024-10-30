class Account:
    TO_ORDER = "[class='card-basic__number']"
    CANCEL_BTN = "[class='button button_block button_xl button_ghost']"
    EMPTY_ORDERS = "[class='j-notification-layout-text']"
    #EMPTY_ORDERS = "//h2[text()='Заказов нет']" #возможен такой локатор <p class="j-notification-layout-text">Ваш заказ отменен</p>, но он быстро исчезает
    CARDS = "//label[text()='Карты']"
    BALANCE = "//div[text()='Баланс']"
    LOG_OUT_BTN ="[class='profile-aside__arrow link link_arrow link_arrow_right']"
    FAVORITES="[id='favorite']"
    PRODUCT_IN_FAVORITES = "[class='small-card__title j-small-card-title']"