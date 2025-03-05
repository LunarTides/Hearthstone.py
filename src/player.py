from .card import Card, CardAbility, CardLocation


class Player:
    """
    Represents a player in the game.

    The player has a hand, deck, board, and graveyard.
    It contains methods to play cards, draw cards, and visualize the board,
    among other things.
    """

    def __init__(self, game):
        """Initialize a player."""
        self.game = game

        self.id = 0
        self.hand: list[Card] = []
        self.deck: list[Card] = []
        self.board: list[Card] = []
        self.graveyard: list[Card] = []

    def opponent(self) -> "Player":
        """Return the opposing player."""
        return (
            self.game.current_player
            if self.game.current_player.id != self.id
            else self.game.next_player
        )

    def is_starting_player(self) -> bool:
        """Return true if this player is the starting player."""
        return self.game.player1 == self

    def is_current_player(self) -> bool:
        """Return true if it is currently this player's turn."""
        return self.game.current_player == self

    def name(self):
        """Return the name of this player."""
        return "Player 1" if self.is_starting_player() else "Player 2"

    def add_to_hand(self, card: Card):
        """Add a card to this player's hand."""
        assert card.owner == self, "Card must be owned by the player."

        self.hand.append(card)
        card.location = CardLocation.HAND

    def visualize_board(self, add_separator=False):
        """Return a string representation of this player's board."""
        # Intro: Board (You) / Board (Opponent)
        intro = "[white]"
        if self.is_current_player():
            intro += "----- Board (You) ------"
        else:
            intro += "--- Board (Opponent) ---"
        intro += "\n"

        # Board: Cards / None
        board = (
            "\n".join([str(card) for card in self.board])
            if len(self.board) > 0
            else "[bright_black]None[/bright_black]"
        )

        # Outro: Separator
        outro = "\n------------------------" if add_separator else ""
        return "".join([intro, board, outro])

    def visualize_hand(self):
        """Return a string representation of this player's hand."""
        return f"[white]--- {self.name()}'s Hand ---\n" + "\n".join(
            [str(card) for card in self.hand]
        )

    def play_card(self, card: Card):
        """Play a card from this player's hand."""
        self.hand.remove(card)

        if card.can_be_on_board():
            card.trigger_ability(CardAbility.BATTLECRY)
            self.summon_card(card)

    def summon_card(self, card: Card):
        """Summon a card onto this player's board."""
        assert card.owner == self, "Card must be owned by the player."
        assert card.can_be_on_board(), "Card cannot be summoned on the board."

        self.board.append(card)
        card.location = CardLocation.BOARD
