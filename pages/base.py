from playwright.sync_api import Page, TimeoutError, Response
from data.environment import host

class Base:
    def __init__(self, page: Page):
        self.page = page


#Метод open осуществляет переход на веб-страницу:
    def open(self, uri) -> Response | None:
        return self.page.goto(f"{host.get_base_url()}{uri}",
        #wait_until='domcontentloaded',
                              timeout=60000)

#Метод input осуществляет ввод значений в поле ввода:
    def input(self, locator, data: str) -> None:
        self.page.locator(locator).type(data)

#Метод click осуществляет клик по элементу:
    def click(self, locator) -> None: #
        self.page.click(locator)

#Добавляем таймаут (можно вставлять между операциями, когда Playwright слишком быстро пробегается)
    def timeout(self, timeout: int) -> None:
        self.page.wait_for_timeout(timeout)

#Метод get_text достает текст из элемента по локатору:
    def get_text(self, element) -> str:  #
        return self.page.locator(element).text_content()

#Метод click_element_by_index позволяет кликнуть на нужный элемент, указав его индекс (если на странице есть несколько элементов с одинаковым локатором):
    def click_element_by_index(self, selector: str, index: int):
        self.page.locator(selector).nth(index).click()

#Метод input_value_by_index позволяет кликнуть на нужное поле с инпутом, указав его индекс:
    def input_value_by_index(self, selector: str, index: int, data: str): #вводим данные в нужные поля по индексу
        self.page.locator(selector).nth(index).fill(data)

    def click_text_by_index(self, text: str, index: int):  # находим элемент(кнопку)с нужным текстом и индексом внутри и кликаем
        self.page.get_by_text(text).nth(index).click()

    def click_by_text(self, text: str):  # находим элемент(кнопку)с нужным текстом внутри и кликаем
        self.page.get_by_text(text).click()