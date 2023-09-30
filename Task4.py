import tkinter as tk
from tkinter import messagebox
import random
#Game Choices
game_choice = ["rock", "paper", "scissors"]

#definig function for player's input
def gammer_choice():
    your_choice = your_choice_entry.get().lower()
    if your_choice in game_choice:
        messagebox.showinfo("Your choice selected", f"Player chose {your_choice}")
        game_choice_list.insert(tk.END, f"Player chose {your_choice}")
    else:
        messagebox.showinfo("Invalid input")

#defining computer's Choice and Game results.
def game_result():
    your_choice = your_choice_entry.get().lower()
    comp_choice = random.choice(game_choice)
    messagebox.showinfo("Computer Chose", f"Computer chose: {comp_choice}")
    game_choice_list.insert(tk.END, f"Computer chose {comp_choice}")

    if your_choice == comp_choice:
        messagebox.showinfo("Game tied", "None of you won")
    elif (your_choice == "rock" and comp_choice == "scissors") or \
         (your_choice == "scissors" and comp_choice == "paper") or \
         (your_choice == "paper" and comp_choice == "rock"):
        messagebox.showinfo("Player won the match", f"Player chose {your_choice}, Computer chose {comp_choice}")
    else:
        messagebox.showinfo("Computer won the match", f"Player chose {your_choice}, Computer chose {comp_choice}")
    your_choice_entry.delete(0,tk.END)

#Main Window for GUI
game = tk.Tk()
game.title("ROCK-PAPER-SCISSORS")

#input field and label for search

your_choice_label = tk.Label(game, text="Choices")
your_choice_label.pack()

your_choice_entry = tk.Entry(game, width=50)
your_choice_entry.pack()

#Creating Butttons

your_choice_button = tk.Button(game, text="Your choice", command=gammer_choice)
your_choice_button.pack(pady=8)

result_button = tk.Button(game, text="Result", command=game_result)
result_button.pack(pady=8)

#List where all games decision desplayed

game_choice_list = tk.Listbox(game, width=45)
game_choice_list.pack()


game.mainloop()