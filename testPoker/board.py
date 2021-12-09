class Board:

    def __init__(self):
        self._cards = []
        self.stack = 0

    @property
    def board_cards(self):
        return self._cards
