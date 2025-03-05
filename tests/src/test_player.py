# ruff: noqa: D103 - undocumented-public-function
from src.game import create_game


def test_opponent():
    game = create_game()

    assert game.player1.opponent() == game.player2
    assert game.player2.opponent() == game.player1


def test_is_starting_player():
    game = create_game()

    assert game.player1.is_starting_player()
    assert not game.player2.is_starting_player()


def test_is_current_player():
    game = create_game()

    assert game.player1.is_current_player()
    assert not game.player2.is_current_player()

    game.end_turn()

    assert not game.player1.is_current_player()
    assert game.player2.is_current_player()


def test_name():
    game = create_game()

    assert game.player1.name() == "Player 1"
    assert game.player2.name() == "Player 2"

    player1 = game.player1
    game.player1 = game.player2

    assert player1.name() == "Player 2"


def test_add_to_hand():
    pass


def test_visualize_board():
    pass


def test_visualize_hand():
    pass


def test_play_card():
    pass


def test_summon_card():
    pass
