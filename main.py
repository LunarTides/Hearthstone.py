from src.game import game
from src.player import Player
from rich import print
import cards


def start_game():
    player1 = Player(game)
    player2 = Player(game)
    game.start(player1, player2)


start_game()

sheep1 = cards.sheep.copy(game.current_player)
sheep2 = cards.sheep.copy(game.current_player)

sheep1.cost = 9

game.current_player.add_to_hand(sheep1)
game.current_player.add_to_hand(sheep2)

game.interact.print_watermark()
print(game.current_player.visualize_hand())
