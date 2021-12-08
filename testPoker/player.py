class Player:
    """A player ran by the computer"""

    def __init__(self, number: int):
        self._cards = []
        self._stack = 5000
        self._number = number
        self._keep_playing = 1
        self.value = 0

    @property
    def player_cards(self):
        return self._cards

    @property
    def player_stack(self):
        return self._stack

    @property
    def keep_playing(self):
        return self._keep_playing

    @keep_playing.setter
    def keep_playing(self, value):
        self._keep_playing = value

    def set_stack(self, value):
        self._stack = value
