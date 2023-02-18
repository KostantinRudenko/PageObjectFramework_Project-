'''
Test Case #4
Description: Check, that if you click right arrow next to content page, game's name on it will change.
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        03/02/23                    Initial version

'''
import pytest
@pytest.mark.TT0004
def test_TT0004(open_browser):
    browser = open_browser
    names = browser.change_page_content()
    assert names[0] != names[1]