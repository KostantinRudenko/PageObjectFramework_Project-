'''
Test Case #3
Description: Check, if you select category, you will see its name on opened page
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        14/02/23                    Initial version

'''
import pytest

@pytest.mark.TT0003
def test_TT0006(open_browser):
    browser = open_browser
    text = browser.category_selection()
    assert text == 'БАШЕННАЯ ЗАЩИТА'