from tkinter import *
# import game
import tkinter as tk

from tkinter.messagebox import showinfo


# Initializing the game
from game import Game

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
        window = Tk()
        window.title("Poker")
        window.geometry("500x500")
        window.maxsize = window.maxsize = (500, 500)

        #Creating Canvas
        canvas_topLeft = Canvas(window, height=500, width=800)
        canvas_topLeft.pack(expand=YES, fill=BOTH, side=TOP, anchor=NW)

        canvas_topRight = Canvas(window, height=500, width=800)
        canvas_topRight.pack(expand=YES, fill=BOTH, side=TOP, anchor=NE)

        #Creating Frame
        left_frame = Frame(canvas_topLeft, bg='green', bd=5)
        left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1, anchor='nw')

        right_frame = Frame(canvas_topRight, bg='light green', bd=5)
        right_frame.place(relx=1, rely=0, relwidth=0.5, relheight=1, anchor='ne')


        label_frame = Frame(left_frame, bg='green', bd=5)
        label_frame.place(relx=0.5, relwidth=0.9, anchor='n')






        # Label
        label_Cards = Label(label_frame,bg='green', text="Vos cartes :", font=("Courrier", 20))
        label_Cards.pack()



        # Card 1
        card1 = PhotoImage(file="cards-assets/{}.gif".format(game.game_user.player_cards[0])).zoom(50).subsample(64)
        button_card1 = Button(left_frame, image=card1, bd=0, relief=SUNKEN, command=None)
        button_card1.place(relx=0.5, rely=5, relwidth=5, relheight=5)
        button_card1.pack()
        # Card 2
        card2 = PhotoImage(file="cards-assets/{}.gif".format(game.game_user.player_cards[1])).zoom(50).subsample(64)
        button_card2 = Button(left_frame, image=card2, bg="light green", bd=0, relief=SUNKEN, command=None)
        button_card2.pack()



        validateButton = Button(text="Valider", master=canvas_topRight, command=self.validateButton)
        validateButton.config(width=10, font=('Helvetica', 10))
        validateButton.pack(side=BOTTOM, anchor=SE)

        #Display
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

'''if __name__ == '__main__':
    g = game()'''
