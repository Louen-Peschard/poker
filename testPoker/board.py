class Board:

    def __init__(self):
        self._cards = []
        self._stack = 0

    @property
    def board_cards(self):
        return self._cards

    @property
    def board_stack(self):
        return self._stack

    def set_stack(self, value):
        self._stack = value
