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
@pytest.mark.parametrize('link_number', [('1'), ('2'), ('3'), ('4'), ('5'),
                                         ('6'), ('7'), ('8'), ('9')])
def test_TT0004(open_browser, link_number):
    browser = open_browser
    results = browser.open_popular_game(link_number)
    assert results[0] is results[1] # result[0] is first name of the game on main page of Steam
                                    # result[1] is second name of the game on main page of this game
    print(results[0])
    print(results[1])
    # Мы потеряли етот тест... навсегда... навсегда... навсегда...
    # НЕДЕЛЯ В КАМ