class Market:
  CITY_YES = "//button[text()='Да']"
  DRUG_INPUT = "[placeholder='Название, действующее вещество']"
  CHOOSE_FROM_LIST = "//mark[text()='Анальгин']"
  ADD_BTN = "//button[text()='В корзину']"
  NUM_INPUT = '[name="phone"]'
  CITY_NO = "//button[text()='Нет']"
  CHOOSE_CITY_FROM_LIST = "[data-name='Казань']"
  OLD_PRICE = "[class='product-card-x__price-old price_old']"
  NEW_PRICE = "[class='product-card-x__price-new price_new']"
  PRODUCT_IN_SEARCH_LIST = "//h4[text()='Дезринит']"

  CONFIRM_DELETE_FROM_CART = "//button[text()='Да']"
  EMPTY_CART = "//h1[text()='Корзина пуста']"
  CHANGED_CITY = "[class='header__location-link']"
  TO_FAVORITES = "//p[text()='Избранное']"
  TO_PROFILE_FOR_AUTH = "//p[text()='Войти на сайт']" #неавторизованный пользователь
  TO_PROFILE = "//p[text()='Мой профиль']" #авторизованный пользователь
  ADD_TO_FAVORITES = "[class='svg-icon header__icon  ']"



