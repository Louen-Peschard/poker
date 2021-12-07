from deck import Deck
from game import Game
import random

if __name__ == '__main__':
    # Demande un seed à l'utilisateur pour "contrôler" le random
    user_seed = input("Spécifiez un seed : ")
    if user_seed == "":
        user_seed = random.randint(0, 424242)   # Random si vide
    random.seed(user_seed)

    game = Game()
    game.start_game()
    game.turn_one()
