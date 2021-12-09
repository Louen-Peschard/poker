from player import Player
from board import Board
from collections import Counter


class Compare:

    def __init__(self, player_cards_to_compare: Player.player_cards, board_cards_to_compare: Board.board_cards):
        self.player_cards = player_cards_to_compare
        self.board_cards = board_cards_to_compare
        self.player_and_board_cards = self.player_cards

    """Compare hand only or hand + board"""

    def board_and_hand_strength(self, number_of_draw):
        cards_draw = number_of_draw
        value = 0
        self.player_and_board_cards = self.player_cards
        for i in range(cards_draw):
            self.player_and_board_cards.append(self.board_cards[i])  # Card list + board

        occurence_result = self.test_occurence(self.player_cards)
        flush_result = self.test_flush(self.player_cards)
        straight_result = self.test_straight(self.player_cards)

        if straight_result == "Royal" and flush_result == "Flush":  # Quinte Flush Royale / Always win
            value += 9000
        elif straight_result == "Straight" and flush_result == "Flush":  # Quinte Flush / Win on Four of a Kind
            value += 8000
        elif occurence_result == "Four of a Kind":  # Four of a Kind / Win on Full House
            value += 7000
        elif occurence_result == "Full House":  # Full House / Win on Flush
            value += 6000
        elif flush_result == "Flush":  # Flush / Win on Straight
            value += 5000
        elif straight_result == "Straight":  # Straight / Win on Three of a Kind
            value += 4000
        elif occurence_result == "Three of a Kind":  # Three of a Kind / Win on Two Pair
            value += 3000
        elif occurence_result == "Two Pair":  # Two Pair / Win on Pair
            value += 2000
        elif occurence_result == "One Pair":  # Pair / Win on High Card
            value += 1000
        for i in range(len(self.player_and_board_cards)):  # Hauteur / Gagne en fonction de la valeur totale des cartes
            value += self.player_and_board_cards[i].card_strength()
        self.player_and_board_cards = self.player_cards
        return value

    """Compare but return Text"""

    def text_combinaison(self, number_of_draw):
        cards_draw = number_of_draw
        self.player_and_board_cards = self.player_cards
        for i in range(cards_draw):
            self.player_and_board_cards.append(self.board_cards[i])  # Card list + board

        occurence_result = self.test_occurence(self.player_cards)
        flush_result = self.test_flush(self.player_cards)
        straight_result = self.test_straight(self.player_cards)

        if straight_result == "Royal" and flush_result == "Flush":  # Quinte Flush Royale / Always win
            return "Quinte Flush Royale"
        elif straight_result == "Straight" and flush_result == "Flush":  # Quinte Flush / Win on Four of a Kind
            return "Quinte Flush"
        elif occurence_result == "Four of a Kind":  # Four of a Kind / Win on Full House
            return "Four of a Kind"
        elif occurence_result == "Full House":  # Full House / Win on Flush
            return "Full"
        elif flush_result == "Flush":  # Flush / Win on Straight
            return "Flush"
        elif straight_result == "Straight":  # Straight / Win on Three of a Kind
            return "Straight"
        elif occurence_result == "Three of a Kind":  # Three of a Kind / Win on Two Pair
            return "Three of a Kind"
        elif occurence_result == "Two Pair":  # Two Pair / Win on Pair
            return "Two Pair"
        elif occurence_result == "One Pair":  # Pair / Win on High Card
            return "One Pair"
        self.player_and_board_cards = self.player_cards
        return "High Card"

    """Order list of card with value"""

    def list_in_value(self, list_parameter):
        list_of_cards = list_parameter
        list_of_value = []
        for i in range(len(list_of_cards)):
            list_of_value.append(list_of_cards[i].card_strength())
        return list_of_value

    """Order list of card with symbole"""

    def list_in_symbole(self, list_parameter):
        list_of_cards = list_parameter
        list_of_symbol = []
        for i in range(len(list_of_cards)):
            list_of_symbol.append(list_of_cards[i].symbol)
        return list_of_symbol

    """Test for Pair, Three of a kind or Four of a Kind"""

    def test_occurence(self, card_list_parameter: list):
        list_to_test = self.list_in_value(card_list_parameter)  # List in Value
        number_of_cards = len(list_to_test)
        list_occurenced = Counter(list_to_test)
        is_four = 0
        is_three = 0
        is_pair = 0
        for i in range(number_of_cards):  # Count occurence
            if list_occurenced[i] == 4:
                is_four = 1
            if list_occurenced[i] >= 3:
                is_three = 1
            if list_occurenced[i] >= 2:
                is_pair += 1

        if is_four == 1:
            return "Four of a Kind"
        elif is_three == 1 and is_pair >= 1:
            return "Full House"
        elif is_three == 1:
            return "Three of a Kind"
        elif is_pair >= 2:
            return "Two Pair"
        elif is_pair == 1:
            return "One Pair"
        else:
            return "High Card"

    """Test for Flush"""

    def test_flush(self, card_list_parameter: list):
        list_to_test = self.list_in_symbole(card_list_parameter)  # List in symbole
        number_of_cards = len(list_to_test)
        list_occurenced = Counter(list_to_test)
        is_flush = 0
        for i in range(number_of_cards):  # Count occurence same color
            if list_occurenced[i] == 5:
                is_flush = 1

        if is_flush == 1:
            return "Flush"
        else:
            return "High Card"

    """Test for Straight and Royal (have to be compare with Flush too=)"""

    def test_straight(self, card_list_parameter: list):
        list_to_test = self.list_in_value(card_list_parameter)  # List in value
        number_of_cards = len(list_to_test)
        list_sorted = sorted(list_to_test)
        is_royal = 0
        is_straight = 0
        if list_sorted[number_of_cards - 1] == 14:
            is_royal = 1
        for i in range(number_of_cards - 1):
            if list_sorted[i] + 1 == list_sorted[i + 1]:
                is_straight += 1

        if is_royal == 1 and is_straight >= 4:
            return "Royal"
        elif is_straight >= 4:
            return "Straight"
        else:
            return "High Card"
