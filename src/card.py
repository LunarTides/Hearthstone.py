from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.player import Player


class CardRarity(Enum):
    FREE = 0
    COMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4


class CardLocation(Enum):
    NONE = 0
    HAND = 1
    DECK = 2
    BOARD = 3
    GRAVEYARD = 4


class Card:
    player: "Player" = None
    location = CardLocation.NONE

    rarity = CardRarity.FREE

    def __init__(self, name: int, cost: int, rarity: CardRarity):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def __str__(self):
        return f"[white][{self.index()}][/white] {self.colorized_name()} [cyan]{{{self.cost}}}[/cyan]"

    def colorized_name(self):
        match self.rarity:
            case CardRarity.FREE:
                return f"[white]{self.name}[/white]"
            case CardRarity.COMMON:
                return f"[bright_black]{self.name}[/bright_black]"
            case CardRarity.RARE:
                return f"[blue]{self.name}[/blue]"
            case CardRarity.EPIC:
                return f"[magenta]{self.name}[/magenta]"
            case CardRarity.LEGENDARY:
                return f"[yellow]{self.name}[/yellow]"

    def copy(self, player: "Player" = None):
        minion = Minion(self.name, self.cost, self.rarity)
        minion.player = player
        return minion

    def index(self):
        match self.location:
            case CardLocation.HAND:
                return self.player.hand.index(self)
            case CardLocation.DECK:
                return self.player.deck.index(self)
            case CardLocation.BOARD:
                return self.player.board.index(self)
            case CardLocation.GRAVEYARD:
                return self.player.graveyard.index(self)


class Minion(Card):
    def __init__(self, name: int, cost: int, rarity: CardRarity):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def __str__(self):
        return f"{Card.__str__(self)}"
