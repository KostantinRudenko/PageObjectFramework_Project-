'''
Test Case #4
Description: Check, that if you click right arrow next to content page, game's name on it will change.
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        17/02/23                    Initial version

'''
import pytest
@pytest.mark.TT0004
def test_TT0004(open_browser):
    browser = open_browser
    name = browser.save_check_name_game()
    assert name[0] == name[2]