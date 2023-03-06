import pytest

from framework.page_object import PageObject

@pytest.fixture(scope='function')
def open_browser():
    browser = PageObject()
    yield browser # return = yield
    browser.close_browser()
    