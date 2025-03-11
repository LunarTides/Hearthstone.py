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

    def visualize_players(self):
        """Return both players' states."""
        player1 = self.game.player1.visualize_state().split("\n")
        player2 = self.game.player2.visualize_state().split("\n")

        # Join the two stats using a "|"
        bricks = [player1[i] + " | " + player2[i] for i in range(len(player1))]
        wall = self.game.utils.create_wall(bricks, "|")

        return "\n".join(wall)
