from player import Player
from deck import Deck


class Game:

    _deck: Deck
    _players: list

    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        for i in range(0, 2):
            player = Player()
            self._players.append(player)

    """First distribution of cards"""
    def start_game(self):
        for i in range(0, 2):
            self._players[i].append(self._deck[0:1])
