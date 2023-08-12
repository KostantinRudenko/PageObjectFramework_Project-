'''
Test Case #5
Description: Check, if incomprehensible game name enter into search field,
the error page will be opened.
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko         14/02/23                    Initial version

'''
import pytest
@pytest.mark.TT0005
@pytest.mark.parametrize('search_text', [('jiefijijefjifejiiefijf'), ('оуашоошуаішщфцщ'), ('ъ')])
def test_TT0005(open_browser, search_text):
    browser = open_browser
    none = browser.text_to_search_field(search_text)
    assert none == '0 results match your search.' or 'Результатов по вашему запросу: 0.'