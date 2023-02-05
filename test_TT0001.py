'''
Test Case #1 
Description: Check, that name of the game was found on the Steam title
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        03/02/23                    Initial version

'''
import pytest
@pytest.mark.TT0001
@pytest.mark.parametrize('name_game', 
                         [('Grand Theft Auto V'), ('Portal 2'),
                          ('Rust'), ('Half-Life 2'), ('RimWorld')]
                        )
def test_TT0001(open_browser, name_game):
    steam_game_title = open_browser
    result = steam_game_title.find_title_game(name_game)
    assert name_game in result