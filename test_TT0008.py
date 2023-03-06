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
    link_numbers = browser.generate_link_numbers(2, 4)
    for link in link_numbers:
        tab_elem = browser.find_tab_elem(link)
        tab_elem.click()
        assert browser.get_title_url() != URL # TODO нужно проверить наличие текста на панелях