'''
Test Case #9
Description: Check that, the price of games from the category "UNDER 80" is less than 80
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko           16/03/23                    Initial version

'''

import pytest

@pytest.mark.TT0009
def test_TT0009(open_browser):
    browser = open_browser
    link_numbers = browser.generate_link_numbers(1, 4)
    for link in link_numbers:
        price = browser.find_price_less_80(link)
        assert price < 80