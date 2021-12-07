from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
from game import Game

# Initializing the game
game = Game()
game.start_game()
for i in range(2):
    print(game.game_user.player_cards[i])


class Interface:

    OptionList = [
        "Action",
        "Raise",
        "Fold",
        "All-in"
    ]

    def __init__(self):
        # Creating the window
        window = Tk()
        window.title("Poker")
        window.geometry("500x500")
        window.minsize = window.maxsize = (500, 500)

        # Creating Canvas
        canvas_top_left = Canvas(window, height=500, width=800)
        canvas_top_left.pack(expand=YES, fill=BOTH, side=TOP, anchor=NW)

        canvas_top_right = Canvas(canvas_top_left, height=500, width=800)
        canvas_top_right.pack(expand=YES, fill=BOTH, side=TOP, anchor=NE)

        # Creating frames
        left_frame = Frame(canvas_top_left, bg='green', bd=5)
        left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1, anchor='nw')

        right_frame = Frame(canvas_top_right, bg='light green', bd=5)
        right_frame.place(relx=1, rely=0, relwidth=0.5, relheight=1, anchor='ne')

        label_frame = Frame(left_frame, bg='green', bd=5)
        label_frame.place(relx=0.5, relwidth=0.9, anchor='n')

        label_board_frame = Frame(right_frame, bg='light green', bd=5)
        label_board_frame.place(relx=0.5, relwidth=1.5, anchor='n')

        # Labels
        label_Cards = Label(label_frame, bg='green', text="Vos cartes :", font=("Courrier", 20))
        label_Cards.pack()
        label_Boards_Cards = Label(label_board_frame, bg='light green', text="Board :", font=("Courrier", 20))
        label_Boards_Cards.pack()

        # Card 1 Hand
        card1Hand = PhotoImage(file="cards-assets/{}.gif".format(game.game_user.player_cards[0])).zoom(50).subsample(64)
        button_card1 = Button(label_frame, image=card1Hand, bd=0, relief=SUNKEN, command=None)
        button_card1.place(relx=0.5, rely=5, relwidth=5, relheight=5)
        button_card1.pack()
        # Card 2 Hand
        card2Hand = PhotoImage(file="cards-assets/{}.gif".format(game.game_user.player_cards[1])).zoom(50).subsample(64)
        button_cardHand2 = Button(label_frame, image=card2Hand, bg="light green", bd=0, relief=SUNKEN, command=None)
        button_cardHand2.place(relx=0.5, rely=5, relwidth=5, relheight=5)
        button_cardHand2.pack()

        # Card 1 Board
        card1Board = PhotoImage(file="cards-assets/{}.gif".format(game._board.board_cards[0])).zoom(50).subsample(64)
        button_cardBoard1 = Button(label_board_frame, image=card1Board, bd=0, relief=SUNKEN, command=None)
        button_cardBoard1.place(relx=0.5, rely=5, relwidth=5, relheight=5)
        button_cardBoard1.pack()

        # Card 2 Board
        card2Board = PhotoImage(file="cards-assets/{}.gif".format(game._board.board_cards[1])).zoom(50).subsample(64)
        button_cardBoard2 = Button(label_board_frame, image=card2Board, bd=0, relief=SUNKEN, command=None)
        button_cardBoard2.place(relx=0.5, rely=5, relwidth=5, relheight=5)
        button_cardBoard2.pack()

        # Card 3 Board
        card3Board = PhotoImage(file="cards-assets/{}.gif".format(game._board.board_cards[2])).zoom(50).subsample(64)
        button_cardBoard3 = Button(label_board_frame, image=card3Board, bd=0, relief=SUNKEN, command=None)
        button_cardBoard3.place(relx=0.5, rely=5, relwidth=5, relheight=5)
        button_cardBoard3.pack()

        # Button
        validateButton = Button(text="Valider", master=canvas_top_right, command=self.validateButton)
        validateButton.config(width=10, font=('Helvetica', 10))
        validateButton.pack(side=BOTTOM, anchor=SE)

        # Display
        window.mainloop()

    def optionList(self):
        # TODO Faire l'action des choix du dropdown menu
        print("Action de la dropdown List")

        # TODO Récupérer l'indice 1 de l'Option List
        '''if mylistbox.get(ANCHOR):
            {
                print("Vous avez choisi de Raise")
            }'''
        # TODO Récupérer l'indice 2 de l'Option List
        '''elif self.OptionList[2]:
            {
                print("Vous avez choisi de Fold")
            }'''
        # TODO Récupérer l'indice 3 de l'Option List
        '''elif self.OptionList[3]:
            {
                print("Vous avez choisi de All-In")
            }'''
        '''else:
          
          {
               print("Veuillez choisir une action")
            }'''

    def validateButton(self):
        # TODO Faire l'action valider du bouton
        print("Action du bouton valider")


if __name__ == '__main__':
    i = Interface()
