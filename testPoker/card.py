class Card:
    """A poker card with a symbol and a value"""

    def __init__(self, symbol, value):
        self._symbol = symbol
        self._value = value

    def __str__(self):
        return self._value + self._symbol

    @property
    def symbol(self):
        return self._symbol

    @property
    def value(self):
        return self._value

    def card_strength(self):
        value = 0
        if self._value == "V":
            value = 11
        elif self._value == "Q":
            value = 12
        elif self._value == "K":
            value = 13
        elif self._value == "A":
            value = 14
        elif 2 <= int(self._value) <= 10:
            value = int(self._value)
        return value

    def card_symbol(self):
        return self._symbol
