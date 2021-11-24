from tkinter import *
from game import Game

# Initializing the game
game = Game()
game.start_game()
for i in range(2):
    print(game.game_user.player_cards[i])

# Creating the window
window = Tk()
window.title("Poker")
window.geometry("500x500")
window.maxsize = window.maxsize = (500, 500)

# Creating the frame
frame = Frame(window)

# Label
label = Label(frame, text="Vos cartes :", font=("Courrier", 30))
label.pack()

# Creating the picture
width = 71
height = 96
# Card 1
card1 = PhotoImage(file="cards-assets/{}.gif".format(game.game_user.player_cards[0])).zoom(50).subsample(64)
button_card1 = Button(frame, image=card1, bd=0, relief=SUNKEN, command=None)
button_card1.pack()
# Card 2
card2 = PhotoImage(file="cards-assets/{}.gif".format(game.game_user.player_cards[1])).zoom(50).subsample(64)
button_card2 = Button(frame, image=card2, bd=0, relief=SUNKEN, command=None)
button_card2.pack()

# Adding frame
frame.pack(expand=YES)

# Display
window.mainloop()
