from playwright.sync_api import Page
from data.environment import host
from playwright.sync_api import expect
from pages.base import Base

class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

#check_url проверяет, что находится на нужной нам странице:
    def check_URL(self, uri, msg):
        expect(self.page).to_have_url(f"{host.get_base_url()}{uri}", timeout=30000), msg

#check_presence проверяет, что элемент присутствует на странице (если есть — то assert True).
    def check_presence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=12000), msg

#check_absence проверяет, что элемент отсутствует на странице (если нет — то assert True).
    def check_absence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_hidden(timeout=700), msg

#have_text проверяет, что у элемента нужный текст
    def have_text(self, locator, text: str, msg):
        loc = self.page.locator(locator)
        expect(loc).to_have_text(text), msg