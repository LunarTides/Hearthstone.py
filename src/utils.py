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

    def align_columns(self, columns, separator):
        """
        Align columns by padding them with spaces.

        This function takes a list of strings and pads them with spaces to make them
        the same length.

        >>> align_columns(["Short | Long", "Longer | Doesn't matter", "A | B"], "|")
        ["Short  | Long", "Longer | Doesn't matter", "A      | B"]

        """
        longest_column = max(
            columns, key=lambda x: len(self.strip_color_tags(x.split(separator)[0]))
        )

        aligned_columns = []
        for column in columns:
            left, right = column.split(separator)
            difference = len(
                self.strip_color_tags(longest_column.split(separator)[0])
            ) - len(self.strip_color_tags(left))

            aligned_columns.append(left + " " * difference + separator + right)

        return aligned_columns

    def strip_color_tags(self, string):
        """Remove color tags from a string."""
        return re.sub(r"\[.+?\]", "", string)
