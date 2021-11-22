class Board:

    def __init__(self):
        self.cards = []
        self.stack = 0

    @property
    def board_cards(self):
        return self.cards
