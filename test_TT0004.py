'''
Test Case #4
Description: Check, that name of game's tab is same to the name of the game on its main page
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
    assert name[0] == name[1]