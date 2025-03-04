import random

from .player import Player
from .interact import Interact


class Game:
    starting_player: Player = None

    current_player: Player = None
    next_player: Player = None

    interact: Interact = None

    def __init__(self):
        self.interact = Interact(self)

    def start(self, player1: Player, player2: Player):
        # Set a random player to be the starting player.
        self.starting_player = random.choice([player1, player2])
        self.current_player = self.starting_player
        self.next_player = player1 if self.current_player == player2 else player2


game = Game()
