from player import Player
from deck import Deck


class Game:


    def __init__(self):
        self._players = []
        self._deck = Deck()
        self._deck.shuffle()
        for i in range(4):
            player = Player(i)
            self._players.append(player)

    """First distribution of cards"""
    def start_game(self):
        for i in range(4):
            for j in range(2):
                self._players[i].cards.append(self._deck.cards.pop(0))
                print(self._players[i].cards[j])




g = Game()
g.start_game()
