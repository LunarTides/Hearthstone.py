from src.card import CardClass, CardRarity, Minion, MinionTribe

sheep1 = Minion(
    # - Common -
    name="Sheep",
    text="",
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
