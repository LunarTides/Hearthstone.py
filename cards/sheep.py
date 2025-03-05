from src.card import Card, CardAbility, CardClass, CardRarity, Minion, MinionTribe

sheep1 = Minion(
    # - Common -
    name="Sheep",
    text="[b]Battlecry:[/b] Add a copy of this minion to your hand which costs 1 more.",
    cost=1,
    classes=[CardClass.NEUTRAL],
    rarities=[CardRarity.FREE],
    collectible=False,
    tags=[],
    unique_id=1,
    # - Minion -
    attack=1,
    health=1,
    tribes=[MinionTribe.BEAST],
)


def battlecry(self, game, owner):
    """Battlecry: Add a copy of this minion to your hand which costs 1 more."""
    card = Card.from_unique_id(1).copy(owner)
    card._cost = self.cost + 1
    owner.add_to_hand(card)


sheep1.add_ability(
    CardAbility.BATTLECRY,
    battlecry,
)
