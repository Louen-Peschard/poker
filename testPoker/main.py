from deck import Deck

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    for i in range(0, len(deck.cards)):
        print(deck.cards[i])
