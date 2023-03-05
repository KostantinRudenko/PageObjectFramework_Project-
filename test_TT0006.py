'''
Test Case #6
Description: Check, if discounts are numbers
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        27/02/23                    Initial version

'''
import pytest

@pytest.mark.TT0006
@pytest.mark.parametrize('link_number', [('1'), ('2'), ('3'), ('4'), ('5'),
                                         ('6'), ('7'), ('8'), ('9'), ('10')])
def test_TT0006(open_browser, link_number):
    browser = open_browser
    number = browser.check_discounts(link_number)
    assert isinstance(number, int) # This function check types
    assert number < 0