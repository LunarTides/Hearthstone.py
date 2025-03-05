class CommandError(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidCommandError(CommandError):
    def __init__(self, command: str):
        super().__init__(f"Invalid command: {command}")


class Commands:
    def __init__(self, game):
        self.game = game

    def handle(self, command: str, args: list[str]):
        if not hasattr(self, command):
            raise InvalidCommandError(command)

        getattr(self, command)(args)

    def end(self, args: list[str]):
        self.game.end_turn()
