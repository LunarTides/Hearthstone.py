import random

from .commands import Commands
from .interact import Interact
from .player import Player
from .utils import Utils


class Game:
    """
    Represents a game of Hearthstone.py.

    You can access most parts of the game, among other classes,
    using the `game` variable.
    """

    player1: Player = None
    player2: Player = None

    current_player: Player = None
    next_player: Player = None

    interact: Interact = None
    utils: Utils = None
    commands: Commands = None

    running = True

    def __init__(self):
        """Initialize the game."""
        self.interact = Interact(self)
        self.utils = Utils(self)
        self.commands = Commands(self)

    def start(self, player1: Player, player2: Player):
        """Set up the game and start it."""
        # Set a random player to be the starting player.
        self.player1 = random.choice([player1, player2])
        self.player2 = player1 if self.player1 == player2 else player2

        self.current_player = self.player1
        self.next_player = self.player2

        self.current_player.id = 0
        self.next_player.id = 1

        # Set starting player's mana
        self.player1.add_empty_mana(1)
        self.player1.mana = 1

    def end_turn(self):
        """End the current player's turn and starts the next player's turn."""
        # We need to create these variables to maintain a reference to both players.
        # Otherwise, we would lose one of them.
        current_player = self.current_player
        next_player = self.next_player

        # Mana
        next_player.add_empty_mana(1)
        next_player.mana = next_player.empty_mana

        self.current_player = next_player
        self.next_player = current_player


def create_game():
    """Create a new game, start it, and return it."""
    game = Game()

    player1 = Player(game)
    player2 = Player(game)

    game.start(player1, player2)
    return game
