class Player:
    """A player ran by the computer"""

    def __init__(self, *args):
        self.cards = []
        self.stack = 5000
        self.number = args
        self.keep_playing = 1
        self.value = 0

    @property
    def player_cards(self):
        return self.cards
