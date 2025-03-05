# ruff: noqa: D103 - undocumented-public-function
from src.game import Game
from src.player import Player


def test_name():
    game = Game()

    player1 = Player(game)
    player2 = Player(game)

    game.start(player1, player2)

    assert game.player1.name() == "Player 1"
    assert game.player2.name() == "Player 2"

    player1 = game.player1
    game.player1 = game.player2

    assert player1.name() == "Player 2"
