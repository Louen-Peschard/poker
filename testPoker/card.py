class Card:
    """A poker card with a symbol and a value"""

    def __init__(self, symbol, value):
        self._symbol = symbol
        self._value = value

    def __str__(self):
        return self._value + " " + self._symbol

    @property
    def symbol(self):
        return self._symbol

    @property
    def value(self):
        return self._value
