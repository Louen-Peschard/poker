from player import Player
from board import Board


class Compare:
    """Compare hand only or hand + board"""

    def __init__(self):
        self.player_cards = Player.player_cards
        self.board_cards = Board.board_cards
        self.value = 0


    def hand_strength(self):
        value = 0
        card_one_value = self.player_cards[0].card_strength()
        card_two_value = self.player_cards[1].card_strength()

        if card_one_value == card_two_value:
            value += 20
        if self.player_cards[0].card.symbol == self.player_cards[0].card.symbol:
            value += 10

        value += card_two_value + card_two_value

        return value

