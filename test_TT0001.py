'''
Test Case #1 
Description: Check, that page's title have name of the game
Resources: Main page

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko        03\02\23                    Initial version

'''
import pytest
@pytest.mark.TT0001
@pytest.mark.parametrize('name_game', 
                         [('Grand Thaft Auto V'), ('Portal 2'),
                          ('Rust'), ('Half Life 2'), ('RimWorld')]
                        )
def test_title(find_game, name_game):
    steam_game_title = find_game
    assert name_game in steam_game_title