import pytest

from framework.page_object import PageObject

@pytest.fixture(scope='function')
def open_browser():
    browser = PageObject()
    yield browser # return = yield
    # тута закрыть браузер 

# НАШО?
def return_title():
    browser = PageObject()
    return browser.find_GTAV()