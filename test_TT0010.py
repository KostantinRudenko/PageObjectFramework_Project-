'''
Test Case #9
Description: Check that, if you click one of category buttons, corresponding page will open
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko           16/03/23                    Initial version

'''

import pytest
@pytest.mark.TT0010
def test_TT0010(open_browser):
    browser = open_browser
    link_numbers = browser.generate_link_numbers(1, 4)
    for link in link_numbers:
        result = browser.click_category(link)
        assert result[0] in result[1]