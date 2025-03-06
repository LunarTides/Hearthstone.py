# ruff: noqa: D103 - undocumented-public-function
from src.game import create_game


def test_create_game():
    game = create_game()

    assert game.player1 == game.current_player
    assert game.player2 == game.next_player

    assert game.current_player.id == 0
    assert game.next_player.id == 1

    assert game.running


def test_end_turn():
    game = create_game()

    assert game.current_player == game.player1
    assert game.next_player == game.player2

    game.end_turn()

    assert game.current_player == game.player2
    assert game.next_player == game.player1
