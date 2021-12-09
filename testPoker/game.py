from player import Player
from deck import Deck
from board import Board
from compare import Compare


class Game:

    def __init__(self):
        # Id of user player
        self._player_user = 3
        # Number of AI players
        self._players_number = 3
        #Numbet of players
        self._all_player_number = 4
        # Number of cards in hand
        self._players_cards = 2
        # Number of cards in board
        self._board_cards = 5
        self._players = []
        self._deck = Deck()
        self._deck.shuffle()
        self._board = Board()
        self._current_bet = 0
        for i in range(self._all_player_number):
            player = Player(i)
            self._players.append(player)

    def start_game(self):
        """First distribution of cards"""
        # For players
        for i in range(self._all_player_number):
            print("Cartes du joueur " + str(i) + " :")
            for j in range(self._players_cards):
                self._players[i].player_cards.append(self._deck.cards.pop(0))
                print(self._players[i].player_cards[j])
            print("------------")
        # For the board
        print("Cartes de la table :")
        for i in range(self._board_cards):
            self._board.board_cards.append(self._deck.cards.pop(0))
            print(self._board.board_cards[i])

    def bet_choice(self, player_number, turn):
        print("Joueur : " + str(player_number))
        if player_number == self._player_user:
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
            for i in range(self._players_cards):
                print(self._players[player_number].player_cards[i])
            Game.bet_choice(self, player_number, turn)

        else:
            print("Error 404 : Try again")
            Game.bet_choice(self, player_number, turn)

    def bet(self, player_number, turn):
        if player_number == self._player_user:
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
            self._board.stack += self.user_bet
            self._players[player_number].player_stack -= self.user_bet

        else:
            self._board.stack += self.user_bet
            self._players[player_number].set_stack(self._players[player_number].player_stack - self.user_bet)

        self._current_bet = self.user_bet

    def turn_one(self):
        turn = 1
        self._board_cards = 0
        # Counter = number of players who fold
        counter = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 0:
                counter += 1
        if counter >= 3:
            Game.turn_final(self)
        else:
            if self._players[self._player_user].keep_playing == 1:
                Game.bet_choice(self, self._player_user, turn)
            for i in range(self._players_number):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, turn)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_two(self)

    def turn_two(self):
        turn = 2
        self._board_cards = 3
        # Counter = number of players who fold
        counter = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 0:
                counter += 1
        if counter >= 3:
            Game.turn_final(self)
        else:
            print("Carte en jeu : ")
            for i in range(self._board_cards):
                print(self._board.board_cards[i])
            if self._players[self._player_user].keep_playing == 1:
                Game.bet_choice(self, self._player_user, turn)
            for i in range(self._players_number):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, turn)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_three(self)

    def turn_three(self):
        turn = 3
        self._board_cards = 4
        # Counter = number of players who fold
        counter = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 0:
                counter += 1
        if counter >= 3:
            Game.turn_final(self)
        else:
            print("Carte en jeu : ")
            for i in range(self._board_cards):
                print(self._board.board_cards[i])
            if self._players[self._player_user].keep_playing == 1:
                Game.bet_choice(self, self._player_user, turn)
            for i in range(self._players_number):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, self._players_number)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_four(self)

    def turn_four(self):
        turn = 4
        self._board_cards = 5
        # Counter = number of players who fold
        counter = 0
        for i in range(self._players_number):
            if self._players[i].keep_playing == 0:
                counter += 1
        if counter == 3:
            Game.turn_final(self)
        else:
            print("Carte en jeu : ")
            for i in range(self._board_cards):
                print(self._board.board_cards[i])
            if self._players[self._player_user].keep_playing == 1:
                Game.bet_choice(self, self._player_user, turn)
            for i in range(self._players_number):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, turn)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_final(self)

    def turn_final(self):
        self._board_cards = 5
        winner = 0
        for i in range(self._all_player_number):
            if self._players[i].keep_playing == 1:

                self._players[i].value = Compare(self._players[i].cards,
                                                 self._board.board_cards).board_and_hand_strength(self._board_cards)
                print("Joueur " + str(i) + " :")
                print(self._players[i].value)
                if winner < self._players[i].value:
                    winner = self._players[i].value
        for i in range(self._all_player_number):
            if winner == self._players[i].value and self._players[i].keep_playing == 1:
                print('Player ' + str(i) + ' win ' + str(self._board.stack))
                print(Compare(self._players[i].cards, self._board.board_cards).text_combinaison(self._board_cards))
                self._players[i].set_stack(self._players[i].player_stack + self._board.stack)
                self._board.stack = 0

    @property
    def game_user(self):
        return self._players[3]
