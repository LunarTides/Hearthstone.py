# ruff: noqa: D103 - undocumented-public-function
from src.card import Card, CardAbility, CardLocation, CardRarity, Minion
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
    card = Card.from_unique_id(1)

    card.rarities = [CardRarity.FREE]
    assert card.colorized_name() == "[white]Sheep[/white]"

    card.rarities = [CardRarity.COMMON]
    assert card.colorized_name() == "[bright_black]Sheep[/bright_black]"

    card.rarities = [CardRarity.RARE]
    assert card.colorized_name() == "[blue]Sheep[/blue]"

    card.rarities = [CardRarity.EPIC]
    assert card.colorized_name() == "[magenta]Sheep[/magenta]"

    card.rarities = [CardRarity.LEGENDARY]
    assert card.colorized_name() == "[yellow]Sheep[/yellow]"


def test_copy():
    card: Minion = Card.from_unique_id(1)
    assert card is not Minion

    new_card = card.copy(None)
    new_card.attack = card.attack + 1

    assert new_card is not card
    assert new_card.attack == card.attack + 1


def test_index():
    game = create_game()
    card: Minion = Card.from_unique_id(1).copy(game.player1)

    game.player1.add_to_hand(card)

    assert game.player1.hand[0] == card
    assert card.location == CardLocation.HAND
    assert card.index() == 0

    game.player1.hand.insert(0, card.copy(game.player1))

    assert game.player1.hand[1] == card
    assert card.location == CardLocation.HAND
    assert card.index() == 1


def test_can_be_on_board():
    card: Minion = Card.from_unique_id(1).copy(None)

    assert card.can_be_on_board()

    # TODO: Test other card types when they are implemented.


def test_trigger_ability():
    game = create_game()

    card: Minion = Card.from_unique_id(1).copy(game.player1)
    card.abilities = {}

    triggered_battlecry = [False]

    card.add_ability(
        CardAbility.BATTLECRY,
        lambda self, game, owner: triggered_battlecry.__setitem__(0, True),
    )

    card.trigger_ability(CardAbility.BATTLECRY)
    assert triggered_battlecry[0]
