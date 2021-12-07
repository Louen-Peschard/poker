from player import Player
from deck import Deck
from board import Board
from compare import Compare


class Game:

    def __init__(self):
        # The real player
        self._user = Player()
        self._players = []
        self._deck = Deck()
        self._deck.shuffle()
        self._board = Board()
        self.current_bet = 0
        # TODO : remplacer 4 joueurs par 3
        for i in range(4):
            player = Player(i)
            self._players.append(player)

    """First distribution of cards"""

    def start_game(self):
        for i in range(4):
            print("Cartes du joueur " + str(i) + " :")
            for j in range(2):
                self._players[i].cards.append(self._deck.cards.pop(0))
                print(self._players[i].cards[j])
            print("------------")  # ne sert qu'à rendre le terminal plus lisible

        # print("Cartes de la table :")
        for i in range(5):
            self._board.cards.append(self._deck.cards.pop(0))
            print(self._board.cards[i])
            # Pour vérifier les cartes

    def bet_choice(self, player_number, turn):
        print("Joueur : " + str(player_number))
        if player_number == 3:
            self.user_choice = str(input("Miser | Suivre | Check | Se coucher | Afficher son jeu "))
        else:
            if turn == 1:  # Choix des IA tour 1
                handValue = Compare(self._players[player_number].player_cards,
                                    self._board.board_cards).board_and_hand_strength(0)
                if handValue >= 25:
                    self.user_choice = "Miser"
                elif handValue >= 17:
                    self.user_choice = "Suivre"
                elif handValue >= 10 and self.current_bet == self._players[player_number].stack:
                    self.user_choice = "Check"
                else:
                    self.user_choice = "Se coucher"

            elif turn == 2:  # Choix des IA tour 2
                handValue = Compare(self._players[player_number].player_cards,
                                    self._board.board_cards).board_and_hand_strength(3)
                if handValue >= 1000:
                    self.user_choice = "Miser"
                elif handValue >= 40:
                    self.user_choice = "Suivre"
                elif handValue >= 20 and self.current_bet == self._players[player_number].stack:
                    self.user_choice = "Check"
                else:
                    self.user_choice = "Se coucher"

            elif turn == 3:  # Choix des IA tour 3
                handValue = Compare(self._players[player_number].player_cards,
                                    self._board.board_cards).board_and_hand_strength(4)
                if handValue >= 2000:
                    self.user_choice = "Miser"
                elif handValue >= 60:
                    self.user_choice = "Suivre"
                elif handValue >= 30 and self.current_bet == self._players[player_number].stack:
                    self.user_choice = "Check"
                else:
                    self.user_choice = "Se coucher"

            elif turn == 4:  # Choix des IA tour 4
                handValue = Compare(self._players[player_number].player_cards,
                                    self._board.board_cards).board_and_hand_strength(5)
                if handValue >= 3000:
                    self.user_choice = "Miser"
                elif handValue >= 1000:
                    self.user_choice = "Suivre"
                elif handValue >= 50 and self.current_bet == self._players[player_number].stack:
                    self.user_choice = "Check"
                else:
                    self.user_choice = "Se coucher"
        print(self.user_choice)

        #Ajout du Bet
        if self.user_choice == "Miser":
            Game.bet(self, player_number, turn)

        elif self.user_choice == "Suivre":
            self._board.stack += self.current_bet
            self._players[player_number].stack -= self.current_bet

        elif self.user_choice == "Check":
            if self._players[player_number].stack == self.current_bet:
                print("Check")

        elif self.user_choice == "Se coucher":
            self._players[player_number].keep_playing = 0

        elif self.user_choice == "Afficher son jeu":
            for i in range(2):
                print(self._players[player_number].cards[i])
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

        if self.user_bet < self.current_bet:
            print("Vous devez miser à la hauteur de la mise actuelle")
            Game.bet_choice(self, player_number, turn)

        if self._players[player_number].stack < self.user_bet:
            print("Vous ne pouvez pas miser autant !")
            Game.bet_choice(self, player_number, turn)

        elif self._players[player_number].stack == self.user_bet:
            print("Tapis !")
            self._board.stack += self.user_bet
            self._players[player_number].stack -= self.user_bet

        else:
            self._board.stack += self.user_bet
            self._players[player_number].stack -= self.user_bet

        self.current_bet = self.user_bet

    def turn_one(self):
        compteur = 0
        for i in range(4):
            if self._players[i].keep_playing == 0:
                compteur += 1
        if compteur >= 3:
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
        compteur = 0
        for i in range(4):
            if self._players[i].keep_playing == 0:
                compteur += 1
        if compteur >= 3:
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
        compteur = 0
        for i in range(4):
            if self._players[i].keep_playing == 0:
                compteur += 1
        if compteur >= 3:
            Game.turn_final(self)
        else:
            print("Carte en jeu : ")
            for i in range(4):
                print(self._board.cards[i])
            if self._players[3].keep_playing == 1:
                Game.bet_choice(self, 3, 3)
            for i in range(3):
                if self._players[i].keep_playing == 1:
                    Game.bet_choice(self, i, 3)
            print("Pot en jeu : " + str(self._board.stack))
            Game.turn_four(self)

    def turn_four(self):
        compteur = 0
        for i in range(4):
            if self._players[i].keep_playing == 0:
                compteur += 1
        if compteur == 3:
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
        for i in range(4):
            if self._players[i].keep_playing == 1:
                self._players[i].value = Compare(self._players[i].player_cards, self._board.board_cards).board_and_hand_strength(5)
                print("Joueur " + str(i) + " :")
                print(self._players[i].value)
                if winner < self._players[i].value:
                    winner = self._players[i].value
        for i in range(4):
            if winner == self._players[i].value and self._players[i].keep_playing == 1:
                print('Player '+str(i)+' win '+str(self._board.stack))
                print(Compare(self._players[i].player_cards, self._board.board_cards).text_combinaison(5))
                self._players[i].stack += self._board.stack
                self._board.stack = 0



    @property
    def game_user(self):
        return self._user
