class CommandError(Exception):
    """Base class for command errors."""

    def __init__(self, message: str):
        """Initialize the command error."""
        self.message = message


class InvalidCommandError(CommandError):
    """An invalid command error."""

    def __init__(self, command: str):
        """Initialize the invalid command error."""
        super().__init__(f"Invalid command: {command}")


class Commands:
    """
    A class for handling commands.

    This also has a function for every command.
    """

    def __init__(self, game):
        """Initialize the commands class."""
        self.game = game

    def handle(self, command: str, args: list[str]):
        """Execute a command if it exists."""
        if not hasattr(self, command):
            raise InvalidCommandError(command)

        getattr(self, command)(args)

    def end(self, args: list[str]):
        """End the current player's turn and starts the next player's turn."""
        self.game.end_turn()
