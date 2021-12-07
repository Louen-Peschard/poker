from player import Player
from board import Board
from collections import Counter


class Compare:
    """Compare hand only or hand + board"""

    def __init__(self, player_cards_to_compare: Player.player_cards, board_cards_to_compare: Board.board_cards):
        self.player_cards = player_cards_to_compare
        self.board_cards = board_cards_to_compare
        self.player_and_board_cards = self.player_cards



    def board_and_hand_strength(self, number_of_draw):
        cards_draw = number_of_draw
        value = 0
        for i in range(cards_draw):
            self.player_and_board_cards.append(self.board_cards[i])  # Liste des cartes joueur + plateau

        occurence_result = self.test_occurence(self.player_cards)
        flush_result = self.test_flush(self.player_cards)
        straight_result = self.test_straight(self.player_cards)

        if straight_result == "Royal" and flush_result == "Flush":  # Quinte Flush Royale / Gagne toujours
            value += 9000
        elif straight_result == "Straight" and flush_result == "Flush":  # Quinte Flush / Gagne sur Carre
            value += 8000
        elif occurence_result == "Four of a Kind":  # Carre / Gagne sur Full
            value += 7000
        elif occurence_result == "Full House":  # Full / Gagne sur Couleur
            value += 6000
        elif flush_result == "Flush":  # Couleur / Gagne sur Suite
            value += 5000
        elif straight_result == "Straight":  # Suite / Gagne sur Brelan
            value += 4000
        elif occurence_result == "Three of a Kind":  # Brelan / Gagne sur Double Paire
            value += 3000
        elif occurence_result == "Two Pair":  # Double Paire / Gagne sur Paire
            value += 2000
        elif occurence_result == "One Pair":  # Paire / Gagne sur Hauteur
            value += 1000
        for i in range(len(self.player_and_board_cards)):  # Hauteur / Gagne en fonction de la valeur totale des cartes
            value += self.player_and_board_cards[i].card_strength()
        return value


    def text_combinaison(self, number_of_draw):
        cards_draw = number_of_draw
        value = 0
        for i in range(cards_draw):
            self.player_and_board_cards.append(self.board_cards[i])  # Liste des cartes joueur + plateau

        occurence_result = self.test_occurence(self.player_cards)
        flush_result = self.test_flush(self.player_cards)
        straight_result = self.test_straight(self.player_cards)

        if straight_result == "Royal" and flush_result == "Flush":  # Quinte Flush Royale / Gagne toujours
            return "Quinte Flush Royale"
        elif straight_result == "Straight" and flush_result == "Flush":  # Quinte Flush / Gagne sur Carre
            return "Quinte Flush"
        elif occurence_result == "Four of a Kind":  # Carre / Gagne sur Full
            return "Carre"
        elif occurence_result == "Full House":  # Full / Gagne sur Couleur
            return "Full"
        elif flush_result == "Flush":  # Couleur / Gagne sur Suite
            return "Flush"
        elif straight_result == "Straight":  # Suite / Gagne sur Brelan
            return "Straight"
        elif occurence_result == "Three of a Kind":  # Brelan / Gagne sur Double Paire
            return "Three of a Kind"
        elif occurence_result == "Two Pair":  # Double Paire / Gagne sur Paire
            return "Two Pair"
        elif occurence_result == "One Pair":  # Paire / Gagne sur Hauteur
            return "One Pair"
        return "Hauteur"

    def list_in_value(self, list_parameter):
        list_of_cards = list_parameter
        list_of_value = []
        for i in range(len(list_of_cards)):
            list_of_value.append(list_of_cards[i].card_strength())
        return list_of_value

    def list_in_symbole(self, list_parameter):
        list_of_cards = list_parameter
        list_of_symbol = []
        for i in range(len(list_of_cards)):
            list_of_symbol.append(list_of_cards[i].card_symbol())
        return list_of_symbol

    def test_occurence(self, card_list_parameter: list):
        list_to_test = self.list_in_value(card_list_parameter)  # liste en valeur pour comparer les occurrence
        number_of_cards = len(list_to_test)
        list_occurenced = Counter(list_to_test)
        is_four = 0
        is_three = 0
        is_pair = 0
        for i in range(number_of_cards):  # compte le nombre d'occurrence
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
            return "Hauteur"

    def test_flush(self, card_list_parameter: list):
        list_to_test = self.list_in_symbole(card_list_parameter)  # liste en symbole pour comparer les couleurs
        number_of_cards = len(list_to_test)
        list_occurenced = Counter(list_to_test)
        is_flush = 0
        for i in range(number_of_cards):  # compte le nombre d'occurrence
            if list_occurenced[i] == 5:
                is_flush = 1

        if is_flush == 1:
            return "Flush"
        else:
            return "Hauteur"

    def test_straight(self, card_list_parameter: list):
        list_to_test = self.list_in_value(card_list_parameter)  # liste en valeur pour comparer les suites
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
            return "Hauteur"
