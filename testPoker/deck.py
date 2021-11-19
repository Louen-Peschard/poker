import constants
import random
from card import Card


class Deck:
    """A stack with all the game's cards"""

    _cards: list

    def __init__(self):
        for i in range(0, len(constants.SYMBOLS)):
            for j in range(0, len(constants.VALUES)):
                card = Card(constants.SYMBOLS[i], constants.VALUES[j])
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    @property
    def cards(self):
        return self._cards
