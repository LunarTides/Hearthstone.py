from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.player import Player


class CardClass(Enum):
    """Represents a Card Class."""

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
    """Represents a Card Rarity."""

    FREE = 0
    COMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4


class CardLocation(Enum):
    """Represents a Card Location. Used for indexing."""

    NONE = 0
    HAND = 1
    DECK = 2
    BOARD = 3
    GRAVEYARD = 4


class CardTag(Enum):
    """Represents a Card Tag. Used for multiple purposes interally."""

    STARTING_HERO = 0
    GALAKROND = 1
    TOTEM = 2
    LACKEY = 3
    QUEST = 4


class Card:
    """
    Represents a card in the game.

    This should not be instantiated directly,
    use `Minion`, `Spell`, `Weapon`, etc... instead.
    """

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
        """Initialize a card."""
        self.name = name
        self.text = text
        self._cost = cost
        self.classes = classes
        self.rarities = rarities
        self.collectible = collectible
        self.tags = tags
        self._unique_id = unique_id

        self.owner: Player = None
        self.location = CardLocation.NONE

    def __str__(self):
        """Return a string representation of this card."""
        index = f"[white][{self.index() + 1}][/white]"
        name = self.colorized_name()
        cost = f"[cyan]{{{self.cost}}}[/cyan]"

        return f"{index} {name} {cost}"

    @staticmethod
    def from_unique_id(unique_id: int) -> "Card":
        """
        Return the card with the given unique id.

        Remember to `copy` the card before using it!
        """
        import cards

        return list(
            filter(
                lambda card: isinstance(card, Card) and card.unique_id == unique_id,
                cards.__dict__.values(),
            )
        )[0]

    @property
    def cost(self):
        """Return the cost of this card."""
        return self._cost

    # @cost.setter
    # def cost(self, value):
    #     """Set the cost of this card."""
    #     # TODO: Add an enchantment.
    #     pass

    @property
    def unique_id(self):
        """Return the unique id of this card."""
        return self._unique_id

    def colorized_name(self):
        """
        Return a colorized name of this card.

        The name is colored based on this card's rarity.
        """
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
        """Return a copy of this card, owned by the given player."""
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

        card.owner = player
        return card

    def index(self):
        """
        Return the index of this card in its owner's list.

        E.g. If this card is in the player's hand,
        returns the index of this card in the player's hand.
        """
        match self.location:
            case CardLocation.HAND:
                return self.owner.hand.index(self)
            case CardLocation.DECK:
                return self.owner.deck.index(self)
            case CardLocation.BOARD:
                return self.owner.board.index(self)
            case CardLocation.GRAVEYARD:
                return self.owner.graveyard.index(self)

    def can_be_on_board(self) -> bool:
        """Return true if this card can be summoned onto the board."""
        return False


class MinionTribe(Enum):
    """Represents a Minion Tribe."""

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
    """
    Represents a minion card in the game.

    Minions have attack, health, and tribes.

    Minions can also be on the board.
    """

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
        """Initialize a minion."""
        super().__init__(
            name, text, cost, classes, rarities, collectible, tags, unique_id
        )

        self.attack = attack
        self.health = health
        self.tribes = tribes

    def __str__(self):
        """Return a string representation of this minion."""
        return f"{super().__str__()}"

    def copy(self, player: "Player" = None):
        """Return a copy of this minion, owned by the given player."""
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

        minion.owner = player
        return minion

    def can_be_on_board(self):
        """Return true."""
        return True
