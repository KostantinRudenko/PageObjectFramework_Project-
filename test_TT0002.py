'''
Test Case #2
Description: Check, that game can be found on Steam
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko       01\29\23                    Initial version

'''

import pytest

@pytest.mark.TT0001
@pytest.mark.parametrize('name_game', ['Grand Theft Auto V', ...])
def test_TT0001(open_browser, name_game):
    browser = open_browser
    title = browser.find_game(name_game)
    assert title == name_game