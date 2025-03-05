from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.player import Player


class CardClass(Enum):
    NEUTRAL = 0
    DEATH_KNIGHT = 1
    DEMON_HUNTER = 2
    DRUID = 3
    HUNTER = 4
    MAGE = 5
    PALADIN = 6
    PRIEST = 7
    ROGUE = 8
    SHAMAN = 9
    WARLOCK = 10
    WARRIOR = 11


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


class CardTag(Enum):
    STARTING_HERO = 0
    GALAKROND = 1
    TOTEM = 2
    LACKEY = 3
    QUEST = 4


class Card:
    def __init__(
        self,
        name: str,
        text: str,
        cost: int,
        classes: list[CardClass],
        rarities: list[CardRarity],
        collectible: bool,
        tags: list[CardTag],
        unique_id: int,
    ):
        self.name = name
        self.text = text
        self._cost = cost
        self.classes = classes
        self.rarities = rarities
        self.collectible = collectible
        self.tags = tags
        self._unique_id = unique_id

        self.player: Player = None
        self.location = CardLocation.NONE

    def __str__(self):
        index = f"[white][{self.index() + 1}][/white]"
        name = self.colorized_name()
        cost = f"[cyan]{{{self.cost}}}[/cyan]"

        return f"{index} {name} {cost}"

    @staticmethod
    def from_unique_id(unique_id: int) -> "Card":
        import cards

        return list(
            filter(
                lambda card: isinstance(card, Card) and card.unique_id == unique_id,
                cards.__dict__.values(),
            )
        )[0]

    @property
    def cost(self):
        return self._cost

    # @cost.setter
    # def cost(self, value):
    #     # TODO: Add an enchantment.
    #     pass

    @property
    def unique_id(self):
        return self._unique_id

    def colorized_name(self):
        match self.rarities[0]:
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

    def copy(self, player: "Player"):
        card = Card(
            name=self.name,
            text=self.text,
            cost=self.cost,
            classes=self.classes,
            rarities=self.rarities,
            collectible=self.collectible,
            tags=self.tags,
            unique_id=self.unique_id,
        )

        card.player = player
        return card

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


class MinionTribe(Enum):
    NONE = 0
    ALL = 1
    BEAST = 2
    DEMON = 3
    DRAGON = 4
    ELEMENTAL = 5
    MECH = 6
    MURLOC = 7
    NAGA = 8
    PIRATE = 9
    QUILBOAR = 10
    TOTEM = 11
    UNDEAD = 12


class Minion(Card):
    attack = 0
    health = 0
    tribes: list[MinionTribe] = []

    def __init__(
        self,
        name: str,
        text: str,
        cost: int,
        classes: list[CardClass],
        rarities: list[CardRarity],
        collectible: bool,
        tags: list[CardTag],
        unique_id: int,
        attack: int,
        health: int,
        tribes: list[MinionTribe],
    ):
        super().__init__(
            name, text, cost, classes, rarities, collectible, tags, unique_id
        )

        self.attack = attack
        self.health = health
        self.tribes = tribes

    def __str__(self):
        return f"{super().__str__()}"

    def copy(self, player: "Player" = None):
        minion = Minion(
            name=self.name,
            text=self.text,
            cost=self.cost,
            classes=self.classes,
            rarities=self.rarities,
            collectible=self.collectible,
            tags=self.tags,
            unique_id=self.unique_id,
            attack=self.attack,
            health=self.health,
            tribes=self.tribes,
        )

        minion.player = player
        return minion
