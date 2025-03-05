# ruff: noqa: D103 - undocumented-public-function
from src.card import Card, Minion
from src.game import create_game


def test_str():
    game = create_game()

    card: Minion = Minion.from_unique_id(1).copy(game.current_player)
    game.current_player.add_to_hand(card)

    assert card is not Minion

    assert (
        str(card)
        == f"[white][1][/white] [cyan]{{{card.cost}}}[/cyan] [white]{card.name}[/white] ({card.text}) [green][{card.attack} / {card.health}][/green] [yellow](Minion)[/yellow]"  # noqa: E501 - TODO: Remove.
    )


def test_from_unique_id():
    card = Card.from_unique_id(1)

    assert card.name == "Sheep"


def test_colorized_name():
    pass


def test_copy():
    pass


def test_index():
    pass


def test_can_be_on_board():
    pass


def test_trigger_ability():
    pass
