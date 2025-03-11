import re


class GameError(Exception):
    """A recoverable error during the game."""

    def __init__(self, message: str):
        """Initialize the command error."""
        self.message = message


class Utils:
    """A class for utility functions."""

    def __init__(self, game):
        """Initialize the utils class."""
        self.game = game

    def create_wall(self, bricks, separator):
        """
        Create a wall.

        Walls are a formatting tool for strings which makes them easier to read.
        """
        longest_brick = max(
            bricks, key=lambda x: len(self.strip_color_tags(x.split(separator)[0]))
        )

        wall = []
        for brick in bricks:
            left, right = brick.split(separator)
            difference = len(
                self.strip_color_tags(longest_brick.split(separator)[0])
            ) - len(self.strip_color_tags(left))

            wall.append(left + " " * difference + separator + right)

        return wall

    def strip_color_tags(self, string):
        """Remove color tags from a string."""
        return re.sub(r"\[.+?\]", "", string)
