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

    def card_strength(self):
        value = 0
        if 2 <= self._value <= 10:
            value = self._value
        elif self._value == "valet":
            value = 11
        elif self._value == "queen":
            value = 12
        elif self._value == "king":
            value = 13
        elif self._value == "ace":
            value = 14
        return value