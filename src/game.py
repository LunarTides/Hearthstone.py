import random

from .commands import Commands
from .interact import Interact
from .player import Player


class Game:
    player1: Player = None
    player2: Player = None

    current_player: Player = None
    next_player: Player = None

    interact: Interact = None
    commands: Commands = None

    running = True

    def __init__(self):
        self.interact = Interact(self)
        self.commands = Commands(self)

    def start(self, player1: Player, player2: Player):
        # Set a random player to be the starting player.
        self.player1 = random.choice([player1, player2])
        self.player2 = player1 if self.player1 == player2 else player2

        self.current_player = self.player1
        self.next_player = self.player2

        self.current_player.id = 0
        self.next_player.id = 1

    def end_turn(self):
        current_player = self.current_player
        next_player = self.next_player

        self.current_player = next_player
        self.next_player = current_player


game = Game()
