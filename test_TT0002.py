'''
Test Case #1 
Description: Check, that you logged in to steam
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        06/02/23                    Initial version

'''
import pytest
@pytest.mark.TT0002
def test_TT0002(open_browser):
    steam = open_browser
    result = steam.steam_login()
    assert 'rudenkokostya10' in result