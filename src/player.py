from .card import Card, CardLocation


class Player:
    def __init__(self, game):
        self.game = game

        self.id = 0
        self.hand: list[Card] = []
        self.deck: list[Card] = []
        self.board: list[Card] = []
        self.graveyard: list[Card] = []

    def opponent(self) -> "Player":
        return (
            self.game.current_player
            if self.game.current_player.id != self.id
            else self.game.next_player
        )

    def is_starting_player(self):
        return self.game.player1 == self

    def is_current_player(self):
        return self.game.current_player == self

    def name(self):
        return "Player 1" if self.is_starting_player() else "Player 2"

    def add_to_hand(self, card: Card):
        assert card.owner == self, "Card must be owned by the player"

        self.hand.append(card)
        card.location = CardLocation.HAND

    def visualize_board(self, add_separator=False):
        intro = "[white]"
        if self.is_current_player():
            intro += "----- Board (You) ------"
        else:
            intro += "--- Board (Opponent) ---"
        intro += "\n"

        board = (
            "\n".join([str(card) for card in self.board])
            if len(self.board) > 0
            else "[bright_black]None[/bright_black]"
        )
        outro = "\n------------------------" if add_separator else ""
        return "".join([intro, board, outro])

    def visualize_hand(self):
        return f"[white]--- {self.name()}'s Hand ---\n" + "\n".join(
            [str(card) for card in self.hand]
        )

    def play_card(self, card: Card):
        self.hand.remove(card)
        self.board.append(card)
        card.location = CardLocation.BOARD
