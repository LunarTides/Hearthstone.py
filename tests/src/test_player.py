# ruff: noqa: D103 - undocumented-public-function
import pytest

from src.card import Card, CardAbility
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
    game = create_game()

    assert len(game.player1.hand) == 0

    card = Card.from_unique_id(1).copy(game.player1)
    game.player1.add_to_hand(card)

    assert len(game.player1.hand) == 1
    assert game.player1.hand[0] == card

    opponent_card = card.copy(game.player2)

    with pytest.raises(AssertionError, match="Card must be owned by the player."):
        game.player1.add_to_hand(opponent_card)


def test_visualize_board():
    game = create_game()

    assert (
        game.player1.visualize_board()
        == "[white]----- Board (You) ------\n[bright_black]None[/bright_black]"
    )

    assert (
        game.player1.visualize_board(True)
        == "[white]----- Board (You) ------\n[bright_black]None[/bright_black]\n------------------------"  # noqa: E501 - TODO: Remove
    )

    assert (
        game.player2.visualize_board()
        == "[white]--- Board (Opponent) ---\n[bright_black]None[/bright_black]"
    )

    assert (
        game.player2.visualize_board(True)
        == "[white]--- Board (Opponent) ---\n[bright_black]None[/bright_black]\n------------------------"  # noqa: E501 - TODO: Remove
    )

    card = Card.from_unique_id(1).copy(game.player1)
    game.player1.summon_card(card)

    assert game.player1.visualize_board() == f"[white]----- Board (You) ------\n{card}"
    assert (
        game.player1.visualize_board(True)
        == f"[white]----- Board (You) ------\n{card}\n------------------------"
    )


def test_visualize_hand():
    game = create_game()

    assert game.player1.visualize_hand() == "[white]--- Player 1's Hand ---\n"
    card = Card.from_unique_id(1).copy(game.player1)
    game.player1.add_to_hand(card)

    assert game.player1.visualize_hand() == f"[white]--- Player 1's Hand ---\n{card}"


def test_play_card():
    game = create_game()

    triggered_battlecry = [False]

    card = Card.from_unique_id(1).copy(game.player1)
    # Remove all abilities.
    card.abilities = {}
    card.add_ability(
        CardAbility.BATTLECRY,
        lambda self, game, owner: triggered_battlecry.__setitem__(0, True),
    )

    game.player1.add_to_hand(card)

    assert len(game.player1.hand) == 1
    assert len(game.player1.board) == 0

    game.player1.play_card(card)

    assert len(game.player1.hand) == 0
    assert len(game.player1.board) == 1

    assert triggered_battlecry[0]


def test_summon_card():
    game = create_game()

    assert len(game.player1.board) == 0

    card = Card.from_unique_id(1).copy(game.player1)
    game.player1.summon_card(card)

    assert len(game.player1.board) == 1
    assert game.player1.board[0] == card

    opponent_card = card.copy(game.player2)

    with pytest.raises(AssertionError, match="Card must be owned by the player."):
        game.player1.summon_card(opponent_card)

    new_card = card.copy(game.player1)
    new_card.can_be_on_board = lambda: False

    with pytest.raises(AssertionError, match="Card cannot be summoned on the board."):
        game.player1.summon_card(new_card)
