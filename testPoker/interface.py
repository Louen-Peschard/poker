from tkinter import *
# import game
import tkinter as tk

from tkinter.messagebox import showinfo


class Interface:
    OptionList = [
        "Action",
        "Raise",
        "Fold",
        "All-in"
    ]

    def __init__(self):
        window = Tk()
        window.title("Projet-Poker")
        window.geometry("400x400")
        # Panel
        p1 = PanedWindow(orient='vertical')
        p1.pack(fill=BOTH, expand=1)
        top = Label(Ap1, bg='green')
        p1.add(top)

        bottom = Label(p1, bg='#7BEE9D')
        p1.add(bottom)

        self.optionList()
        variable = tk.StringVar(bottom)
        variable.set(self.OptionList[0])

        opt = tk.OptionMenu(bottom, variable, *self.OptionList)
        opt.config(width=10, font=('Helvetica', 10))
        opt.pack(side=TOP, anchor=NW)

        validateButton = Button(text="Valider", master=p1, command=self.validateButton)
        validateButton.config(width=10, font=('Helvetica', 10))
        validateButton.pack(side=BOTTOM, anchor=SE)

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
