from tkinter import *
from random import randint


def rock():

    user = "rock"
    turn(user)


def paper():

    user = "paper"
    turn(user)


def scissors():

    user = "scissors"
    turn(user)


def turn(user):

    opp = ['rock', 'paper', 'scissors']
    cpu = opp[randint(0,2)]
    if cpu == user:
        result.configure(text="\n\n\n\nIt's a draw.\n\n\n\n You both choose same")
    elif cpu == 'rock' and user == 'scissors':
        result.configure(text="\n\n\n\nYou are defeated!\n\n\n\nOpponent had Rock")
    elif cpu == 'paper' and user == 'rock':
        result.configure(text="\n\n\n\nYou are defeated!\n\n\n\nOpponent had Paper")
    elif cpu == 'scissors' and user == 'paper':
        result.configure(text="\n\n\n\nYou are defeated!\n\n\n\nOpponent had Scissor")
    elif cpu == 'scissors' and user == 'rock':
        result.configure(text="\n\n\n\nYou Win!\n\n\n\nOpponent had Scissors")
    elif cpu == 'rock' and user == 'paper':
        result.configure(text="\n\n\n\nYou Win!\n\n\n\nOpponent had Rock")
    elif cpu == 'paper' and user == 'scissors':
        result.configure(text="\n\n\n\nYou Win!\n\n\n\nOpponent had Paper")


mainWindow = Tk()
mainWindow.title("Rock-Paper-Scissors")
mainWindow.geometry("800x600")
rockButton = Button(mainWindow, width=20, text="ROCK!", justify=CENTER,
                    command=rock)
paperButton = Button(mainWindow, width=20, text="PAPER!", justify=CENTER,
                     command=paper)
scissorsButton = Button(mainWindow, width=20, text="SCISSORS!", justify=CENTER,
                        command=scissors)
result = Label(mainWindow, width=30, justify=CENTER, font=("Helvetica", 20))
rockButton.grid(row=3, column=1)
paperButton.grid(row=3, column=2)
scissorsButton.grid(row=3, column=3)
result.grid(row=5, column=2)
mainWindow.mainloop()
