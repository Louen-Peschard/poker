
class Player:
    """A player ran by the computer"""

    def __init__(self, player_number):
        self.cards = []
        self.stack = 5000
        self.number = player_number
        self.keep_playing = 1

    @property
    def player_cards(self):
        return self.cards