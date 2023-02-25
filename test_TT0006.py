'''
Test Case #6
Description: Check, if you select category, you will see its name on opened page
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        14/02/23                    Initial version

'''
import pytest

@pytest.mark.TT0006
@pytest.mark.parametrize('column, row, title, expected_text', [('4', '1', 'Башенная защита', 'БАШЕННАЯ ЗАЩИТА')])
def test_TT0006(open_browser, column, row, title, expected_text):
    browser = open_browser
    text = browser.category_select(column, row, title)
    assert text == expected_text