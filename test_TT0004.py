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
@pytest.mark.parametrize('link_number, expected_result',[('1', 'The Last Haven'), ])
def test_TT0004(open_browser, link_number, expected_result):
    browser = open_browser
    browser.open_popular_game(link_number)
    url_name = browser.get_title_url().replace('_', ' ')
    title_name = browser.get_title()
    results = [url_name, title_name]
    for result in results:
        assert expected_result in result
