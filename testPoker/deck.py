import constants
import random
from card import Card


class Deck:
    """A stack with 52 cards"""

    _cards = []

    def __init__(self):
        for i in range(len(constants.SYMBOLS)):
            for j in range(len(constants.VALUES)):
                card = Card(constants.SYMBOLS[i], constants.VALUES[j])
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    @property
    def cards(self):
        return self._cards
