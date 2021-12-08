from player import Player
from deck import Deck
from board import Board
from compare import Compare


class Game:

    def __init__(self):
        # Number of players
        self._players_number = 4
        # _players[0] = user
        self._players = []
        self._deck = Deck()
        self._deck.shuffle()
        self._board = Board()
        self._current_bet = 0
        for i in range(self._players_number):
            player = Player(i)
            self._players.append(player)

    def start_game(self):
        """First distribution of cards"""
        # For players
        for i in range(self._players_number):
            print("Cartes du joueur " + str(i) + " :")
            for j in range(2):
                self._players[i].player_cards.append(self._deck.cards.pop(0))
                print(self._players[i].player_cards[j])
            print("------------")
        # For the board
        print("Cartes de la table :")
        for i in range(5):
            self._board.cards.append(self._deck.cards.pop(0))
            print(self._board.cards[i])

    def bet_choice(self, player_number, turn):
        print("Joueur : " + str(player_number))
        if player_number == 3:
            self.user_choice = str(input("Miser | Suivre | Check | Se coucher | Afficher son jeu "))
        else:
            if turn == 1:  # Choix des IA tour 1
                hand_value = Compare(self._players[player_number].player_cards,
                                    self._board.board_cards).board_and_hand_strength(0)
                if hand_value >= 25:
                    self.user_choice = "Miser"
                elif hand_value >= 17:
                    self.user_choice = "Suivre"
                elif hand_value >= 10 and self._current_bet == self._players[player_number].player_stack:
                    self.user_choice = "Check"
                else:
                    self.user_choice = "Se coucher"

            elif turn == 2:  # Choix des IA tour 2
                hand_value = Compare(self._players[player_number].player_cards,
                                    self._board.board_cards).board_and_hand_strength(3)
                if hand_value >= 1000:
                    self.user_choice = "Miser"
                elif hand_value >= 40:
                    self.user_choice = "Suivre"
                elif hand_value >= 20 and self._current_bet == self._players[player_number].player_stack:
                    self.user_choice = "Check"
                else:
                    self.user_choice = "Se coucher"

            elif turn == 3:  # Choix des IA tour 3
                hand_value = Compare(self._players[player_number].player_cards,
                                    self._board.board_cards).board_and_hand_strength(4)
                if hand_value >= 2000:
                    self.user_choice = "Miser"
                elif hand_value >= 60:
                    self.user_choice = "Suivre"
                elif hand_value >= 30 and self._current_bet == self._players[player_number].player_stack:
                    self.user_choice = "Check"
                else:
                    self.user_choice = "Se coucher"

            elif turn == 4:  # Choix des IA tour 4
                hand_value = Compare(self._players[player_number].player_cards,
                                    self._board.board_cards).board_and_hand_strength(5)
                if hand_value >= 3000:
                    self.user_choice = "Miser"
                elif hand_value >= 1000:
                    self.user_choice = "Suivre"
                elif hand_value >= 50 and self._current_bet == self._players[player_number].player_stack:
                    self.user_choice = "Check"
                else:
                    self.user_choice = "Se coucher"
        print(self.user_choice)

        # Ajout du Bet
        if self.user_choice == "Miser":
            Game.bet(self, player_number, turn)

        elif self.user_choice == "Suivre":
            self._board.stack += self._current_bet
            self._players[player_number].set_stack(self._players[player_number].player_stack - self._current_bet)

        elif self.user_choice == "Check":
            if self._players[player_number].player_stack == self._current_bet:
                print("Check")

        elif self.user_choice == "Se coucher":
            self._players[player_number].keep_playing = 0

        elif self.user_choice == "Afficher son jeu":
            for i in range(2):
                print(self._players[player_number].player_cards[i])
            Game.bet_choice(self, player_number, turn)

        else:
            print("Error 404 : Try again")
            Game.bet_choice(self, player_number, turn)

    def bet(self, player_number, turn):
        if player_number == 3:
            self.user_bet = int(input("Combien voulez-vous miser ? "))
        elif self._board.stack == 0:
            self.user_bet = 20
        else:
            self.user_bet = self.user_bet * 1.5

        if self.user_bet < self._current_bet:
            print("Vous devez miser à la hauteur de la mise actuelle")
            Game.bet_choice(self, player_number, turn)

        if self._players[player_number].player_stack < self.user_bet:
            print("Vous ne pouvez pas miser autant !")
            Game.bet_choice(self, player_number, turn)

        elif self._players[player_number].player_stack == self.user_bet:
            print("Tapis !")
            self._board.player_stack += self.user_bet
            self._players[player_number].player_stack -= self.user_bet

        else:
            self._board.stack += self.user_bet
            self._players[player_number].set_stack(self._players[player_number].player_stack - self.user_bet)

        self._current_bet = self.user_bet

    def turn_one(self):
        counter = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 0:
                counter += 1
        if counter >= 3:
            Game.turn_final(self)
        else:
            if self._players[3].keep_playing == 1:
                Game.bet_choice(self, 3, 1)
            for i in range(3):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, 1)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_two(self)

    def turn_two(self):
        counter = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 0:
                counter += 1
        if counter >= 3:
            Game.turn_final(self)
        else:
            print("Carte en jeu : ")
            for i in range(3):
                print(self._board.cards[i])
            if self._players[3].keep_playing == 1:
                Game.bet_choice(self, 3, 2)
            for i in range(3):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, 2)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_three(self)

    def turn_three(self):
        counter = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 0:
                counter += 1
        if counter >= 3:
            Game.turn_final(self)
        else:
            print("Carte en jeu : ")
            for i in range(self._players_number):
                print(self._board.cards[i])
            if self._players[3].keep_playing == 1:
                Game.bet_choice(self, 3, 3)
            for i in range(3):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, 3)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_four(self)

    def turn_four(self):
        counter = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 0:
                counter += 1
        if counter == 3:
            Game.turn_final(self)
        else:
            print("Carte en jeu : ")
            for i in range(5):
                print(self._board.cards[i])
            if self._players[3].keep_playing == 1:
                Game.bet_choice(self, 3, 4)
            for i in range(3):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, 4)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_final(self)

    def turn_final(self):
        winner = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 1:

                self._players[i].value = Compare(self._players[i].player_cards,
                                                 self._board.board_cards).board_and_hand_strength(5)
                print("Joueur " + str(i) + " :")
                print(self._players[i].value)
                if winner < self._players[i].value:
                    winner = self._players[i].value
        for i in range(self._players_number):
            if winner == self._players[i].value and self._players[i].keep_playing == 1:
                print('Player ' + str(i) + ' win ' + str(self._board.stack))
                self._players[i].set_stack(self._players[i].player_stack + self._board.stack)
                self._board.stack = 0

    @property
    def game_user(self):
        return self._players[0]
