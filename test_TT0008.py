'''
Test Case #8
Description: Check that when clicking on a button, the user is on the corresponding panel
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko                              Initial version

'''

import pytest

from framework.config import URL

@pytest.mark.TT0008
def test_TT0008(open_browser):
    browser = open_browser
    link_numbers = browser.generate_link_numbers(1, 13)
    for link in link_numbers:
        result = browser.find_genre_name(link)
        assert result[0] in result[1] # result[0] - name of genre on the main Steam page
                                      # result[1] - genre's name on its main page