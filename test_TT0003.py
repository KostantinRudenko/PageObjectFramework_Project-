'''
Test Case #3
Description: Check, if you change your languege, you will see inscriptions on
the languege which you have choosen.
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        11/02/23                    Initial version

'''
import pytest

@pytest.mark.TT0003
@pytest.mark.parametrize(['language', 'expected_text'], [('polish', 'Witamy na Steam'),
                                                        ('english', 'Welcome to Steam')])
def test_TT0003(open_browser, language, expected_text):
    browser = open_browser
    polish_title_text = browser.change_language(language)
    assert polish_title_text == expected_text