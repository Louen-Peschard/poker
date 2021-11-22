from player import Player
from deck import Deck
from board import Board


class Game:


    def __init__(self):
        self._players = []
        self._deck = Deck()
        self._deck.shuffle()
        self._board = Board()
        for i in range(4):
            player = Player(i)
            self._players.append(player)

    """First distribution of cards"""
    def start_game(self):
        for i in range(4):
            print("Cartes du joueur " + str(i) + " :")
            for j in range(2):
                self._players[i].cards.append(self._deck.cards.pop(0))
                print(self._players[i].cards[j])
            print("------------")  # ne sert qu'à rendre le terminal plus lisible

        print("Cartes de la table :")
        for i in range(5):
            self._board.cards.append(self._deck.cards.pop(0))
            print(self._board.cards[i])





g = Game()
g.start_game()
