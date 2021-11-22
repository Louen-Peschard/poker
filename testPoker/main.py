from deck import Deck
from game import Game
import random

if __name__ == '__main__':
    # Demande un seed à l'utilisateur pour "contrôler" le random
    user_seed = input("Spécifez un seed : ")
    if user_seed == "":
        user_seed = random.randint(0, 424242)   # Random si vide
    random.seed(user_seed)

    deck = Deck()
    deck.shuffle()
    # for i in range(0, len(deck.cards)):
    #     print(deck.cards[i])

g = Game()
g.start_game()
g.turn_final()
