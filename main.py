from rich import print

import cards
from src.card import Card
from src.commands import CommandError
from src.game import game
from src.player import Player


def start_game():
    player1 = Player(game)
    player2 = Player(game)
    game.start(player1, player2)


start_game()

# Assert that the current player is not the next player
assert game.current_player != game.next_player, (
    "Current player is the next player. Something has gone very wrong."
)

# Two ways to import a card
sheep1 = cards.sheep1.copy(game.current_player)
sheep2 = Card.from_unique_id(1).copy(game.next_player)

# I know :)
sheep1._cost = 9

game.current_player.add_to_hand(sheep1)
game.next_player.add_to_hand(sheep2)

while game.running:
    # Clear screen.
    game.interact.clear_screen()

    print(game.interact.watermark())
    print()
    print(game.player1.visualize_board())
    print(game.player2.visualize_board(True))
    print()
    print(game.current_player.visualize_hand())

    try:
        user = input("\nWhich card do you want to play? ")
    except KeyboardInterrupt:
        game.running = False
        break

    if user == "q":
        game.running = False
        break

    if user.isnumeric():
        user = int(user)
        if user > len(game.current_player.hand):
            print("[red]Invalid card[/red]")
            input()
            continue

        card = game.current_player.hand[user - 1]
        game.current_player.play_card(card)
        continue

    # Parse the command.
    cmd = user.split(" ")[0]
    args = user.split(" ")[1:]

    try:
        game.commands.handle(cmd, args)
    except CommandError as e:
        print(f"[red]{e.message}[/red]")
        input()
        continue
