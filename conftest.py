import pytest

from framework.page_object import PageObject

@pytest.fixture(scope='function')
def open_browser():
    browser = PageObject()
    yield browser.get_title_url(), browser.find_games() # return = yield
    browser.close_browser()