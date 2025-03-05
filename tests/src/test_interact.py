# ruff: noqa: D103 - undocumented-public-function
from src.game import create_game


def test_clear_screen():
    game = create_game()

    # TODO: Actually test.
    game.interact.clear_screen()


def test_watermark():
    game = create_game()

    watermark = game.interact.watermark()

    assert watermark == "Hearthstone.py"
