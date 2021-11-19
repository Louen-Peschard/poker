from deck import Deck
import random

if __name__ == '__main__':

    # Demande un seed à l'utilisateur pour "contrôler" le random
    user_seed = input("Spécifez un seed : ")
    random.seed(user_seed)

    deck = Deck()
    deck.shuffle()
    for i in range(0, len(deck.cards)):
        print(deck.cards[i])
