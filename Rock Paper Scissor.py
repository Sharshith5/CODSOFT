import tkinter as tk
from tkinter import messagebox
import random
root = tk.Tk()
root.title("Rock Paper Scissors")
playerscore = 0
computerscore = 0
def detwinner(playerchoice):
    global playerscore, computerscore
    choices = ["Rock", "Paper", "Scissors"]
    computerchoice = random.choice(choices)
    
    result = ""
    if playerchoice == computerchoice:
        result = "It's a tie/"
    elif (playerchoice == "Rock" and computerchoice == "Scissors") or \
         (playerchoice == "Paper" and computerchoice == "Rock") or \
         (playerchoice == "Scissors" and computerchoice == "Paper"):
        result = f"You win! Computer chose {computerchoice}."
        playerscore += 1
    else:
        result = f"You lose.Computer chose {computerchoice}."
        computerscore += 1
    
    update_score()
    messagebox.showinfo("Result", result)
def update_score():
    playerscore_label.config(text=f"Player Score: {playerscore}")
    computerscore_label.config(text=f"Computer Score: {computerscore}")
def on_button_click(choice):
    detwinner(choice)
rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click("Rock"))
rock_button.grid(row=1, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click("Paper"))
paper_button.grid(row=1, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click("Scissors"))
scissors_button.grid(row=1, column=2, padx=10, pady=10)
playerscore_label = tk.Label(root, text=f"Player Score: {playerscore}")
playerscore_label.grid(row=0, column=0, columnspan=3)

computerscore_label = tk.Label(root, text=f"Computer Score: {computerscore}")
computerscore_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
