'''
Test Case #11
Description: Check that, if you click one of the streams,the page of the game played by the streamer will open
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko           ...                         Initial version

'''

import pytest
@pytest.mark.TT0011

def test_TT0011(open_browser):
    browser = open_browser
    link_numbers = browser.generate_link_numbers(1, 6)
    for link_number in link_numbers:
        names = browser.check_streams(link_number)
        assert names[0] == names[1] # names[0] - name of the streaming game
                                    # names[1] - name of the game on its main page