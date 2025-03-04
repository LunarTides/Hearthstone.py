from .card import Card, CardLocation


class Player:
    hand: list[Card] = []
    deck: list[Card] = []
    board: list[Card] = []
    graveyard: list[Card] = []

    def __init__(self, game):
        self.game = game

    def opponent(self):
        return (
            self.game.current_player
            if self.game.current_player != self
            else self.game.next_player
        )

    def is_starting_player(self):
        return self.game.starting_player == self

    def name(self):
        return "Player 1" if self.is_starting_player() else "Player 2"

    def add_to_hand(self, card: Card):
        self.hand.append(card)
        card.location = CardLocation.HAND

    def visualize_hand(self):
        return "\n".join([str(card) for card in self.hand])
