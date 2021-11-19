from player import Player
from deck import Deck


class Game:


    def __init__(self):
        self._players = []
        self._deck = Deck()
        self._deck.shuffle()
        for i in range(0, 3):
            player = Player(i)
            self._players.append(player)

    """First distribution of cards"""
    def start_game(self):
        for i in range(0, 3):
            for j in range(0, 1):
                self._players[i].cards.append(self._deck.cards.pop(0))

# g = Game()
# g.start_game()
