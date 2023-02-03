'''
Test Case #0
Description: Check, that page is opened
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko       01\22\23                    Initial version

'''

import pytest

@pytest.mark.TT0000
def test_TT0000(open_browser):
    browser = open_browser
    url = browser.get_title_url()
    assert 'store.steampowered.com/' in url
    browser.close_browser()