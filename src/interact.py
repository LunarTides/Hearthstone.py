import os


class Interact:
    """Contains methods for interacting with the user."""

    def __init__(self, game):
        """Initialize the interact class."""
        self.game = game

    def clear_screen(self):
        """Clear the screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def watermark(self):
        """Return a watermark."""
        return "Hearthstone.py"
