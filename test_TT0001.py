'''
Test Case #1 
Description: Check, that name of the game was found on the Steam title
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        03/02/23                    Initial version

'''
import pytest
@pytest.mark.TT0001
def test_TT0001(open_browser):
    browser = open_browser
    link_numbers = browser.generate_link_numbers(0, 6)
    for link in link_numbers:
        result = browser.find_title_game(int(link))
        assert result[0] in result[1] # Result[0] - game name
                                      # Result[1] - title