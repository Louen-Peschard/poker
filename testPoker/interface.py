import tkinter
from tkinter import*
import tkinter as tk
class Interface:
    def __init__(self):
        fenetre = Tk()
        fenetre.title("Projet-Poker")
        fenetre.geometry("400x400")
        # Panel
        p1 = PanedWindow(orient='vertical')
        p1.pack(fill=BOTH, expand=1)
        top = Label(p1, bg='green')
        p1.add(top)

        bottom = Label(p1, bg='#7BEE9D')
        p1.add(bottom)


        OptionList = [
            "Action",
            "Raise",
            "Fold",
            "All-in"
        ]
        variable = tk.StringVar(bottom)
        variable.set(OptionList[0])

        opt = tk.OptionMenu(bottom, variable, *OptionList)
        opt.config(width=10, font=('Helvetica', 10))
        opt.pack(side=TOP, anchor=NW)

        validateButton = Button(text="Validate", master=p1, command=self.validateButton)
        validateButton.config(width=10, font=('Helvetica', 10))
        validateButton.pack(side=BOTTOM, anchor=SE)

        fenetre.mainloop()
        self.optionList()

    def optionList(self):
        #TODO Faire l'action des choix du dropdown menu
        print("Action de la dropdown List")

    def validateButton(self):
        #TODO Faire l'action valider du bouton
        print("Action du bouton valider")

if __name__ == '__main__':
    i = Interface()






