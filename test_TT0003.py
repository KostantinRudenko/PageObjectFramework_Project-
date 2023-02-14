'''
Test Case #3
Description: Check, if you change your language, you will see inscriptions on
the language which you have choosen.
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        11/02/23                    Initial version

'''
import pytest

@pytest.mark.TT0003
@pytest.mark.parametrize(['language', 'expected_text'], [('polish', 'Witamy na Steam'),
                                                        ('english', 'Welcome to Steam'),
                                                        ('italian', 'Benvenuto su STEAM'),
                                                        ('german', 'Willkommen bei Steam!'),
                                                        ('french', 'Benvenuto su STEAM')])
def test_TT0003(open_browser, language, expected_text):
    browser = open_browser
    polish_title_text = browser.change_language(language)
    assert polish_title_text == expected_text