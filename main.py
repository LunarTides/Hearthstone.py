from rich import print

from src.card import Card
from src.commands import CommandError
from src.game import create_game

game = create_game()

# TODO: Remove
sheep1 = Card.from_unique_id(1).copy(game.current_player)
sheep2 = Card.from_unique_id(1).copy(game.next_player)

# I know :)
sheep1._cost = 2

game.current_player.add_to_hand(sheep1)
game.next_player.add_to_hand(sheep2)

while game.running:
    game.interact.clear_screen()

    print(game.interact.watermark())
    print()
    print(game.player1.visualize_board(add_separator=False))
    print(game.player2.visualize_board(add_separator=True))
    print()
    print(game.current_player.visualize_hand())

    try:
        user = input("\nWhich card do you want to play? ")

        # TODO: Remove
        if user == "q":
            game.running = False
            break

        if user.isnumeric():
            user = int(user)
            if user < 1 or user > len(game.current_player.hand):
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
    except KeyboardInterrupt:
        game.running = False
        break
