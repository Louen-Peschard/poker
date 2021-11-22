from player import Player
from deck import Deck
from board import Board


class Game:

    def __init__(self):
        self._players = []
        self._deck = Deck()
        self._deck.shuffle()
        self._board = Board()
        self.current_bet = 0
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
            # print(self._board.cards[i])
            # Pour vérifier les cartes

    def bet_choice(self, player_number):
        print("Joueur : " + str(player_number))
        self.user_choice = str(input("Miser | Suivre | Check | Se coucher "))

        if self.user_choice == "Miser":
            Game.bet(self, player_number)

        elif self.user_choice == "Suivre":
            self._board += self.current_bet
            self._players[player_number].stack -= self.current_bet

        elif self.user_choice == "Check":
            if self._players[player_number].stack == self.current_bet:
                print("Check")

        elif self.user_choice == "Se coucher":
            self._players[player_number].keep_playing = 0

        else:
            self.user_choice = str(input("Miser | Suivre | Check | Se coucher "))

    def bet(self, player_number):
        self.user_bet = int(input("Combien voulez-vous miser ? "))

        if self.user_bet < self.current_bet:
            print("Vous devez miser à la hauteur de la mise actuelle")
            Game.bet_choice(self, player_number)

        if self._players[player_number].stack < self.user_bet:
            print("Vous ne pouvez pas miser autant !")
            Game.bet_choice(self, player_number)

        elif self._players[player_number].stack == self.user_bet:
            print("Tapis !")
            self._board.stack += self.user_bet
            self._players[player_number].stack -= self.user_bet

        else:
            self._board.stack += self.user_bet
            self._players[player_number].stack -= self.user_bet

        self.current_bet = self.user_bet

    def turn_one(self):
        for i in range(4):
            if self._players[i].keep_playing == 1:
                Game.bet_choice(self, i)
        print("Pot en jeu : " + str(self._board.stack))
        Game.turn_two(self)

    def turn_two(self):
        print("Carte en jeu : ")
        for i in range(3):
            print(self._board.cards[i])
        for i in range(4):
            if self._players[i].keep_playing == 1:
                Game.bet_choice(self, i)
        print("Pot en jeu : " + str(self._board.stack))
        Game.turn_three(self)

    def turn_three(self):
        print("Carte en jeu : ")
        for i in range(4):
            print(self._board.cards[i])
        for i in range(4):
            if self._players[i].keep_playing == 1:
                Game.bet_choice(self, i)
        print("Pot en jeu : " + str(self._board.stack))
        Game.turn_four(self)

    def turn_four(self):
        print("Carte en jeu : ")
        for i in range(5):
            print(self._board.cards[i])
        for i in range(4):
            if self._players[i].keep_playing == 1:
                Game.bet_choice(self, i)
        print("Pot en jeu : " + str(self._board.stack))
        Game.turn_final(self)

    def turn_final(self):
        print("fin")
        # Comparaison à faire
        # Affichage du vainqueur


g = Game()
g.start_game()
g.turn_one()
