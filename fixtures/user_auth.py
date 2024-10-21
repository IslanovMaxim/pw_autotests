import pytest
from pages.auth_page import Main


@pytest.fixture(scope='class')
def user_login(browser):
    m = Main(browser)
    m.user_login()