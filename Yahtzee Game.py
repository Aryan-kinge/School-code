# Yahtzee Game Main Program
# Author : Aryan Kinge, Date : December 2018

# Import Libraries
import tkinter as tk
import random
import math
# Create the main window
window = tk.Tk()

# Set the main window title
window.title("Pointless Yahtzee Game")

# Set the main window size in pixels
window.geometry("400x600")

# Ensure that the user cannot resize the window
window.resizable(width=False, height=False)

game_labels = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Chance", "Yahtzee", "Three of a Kind", "Four of a Kind", "Full House", "Small Straight", "Large Straight"]
game_buttons = []
game_scores = []
random_list = [1, 2, 3, 4, 5]
score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
hold_labels = ["Hold 1", "Hold 2", "Hold 3", "Hold 4", "Hold 5", ]
dice_buttons = []
dice_numbers = []


# Define functions
def confirm_players():
    num_players = entry_numplay.get()
    if num_players == "1" or num_players == "2":
        print("Number of players is confirmed as " + num_players)
        label_numplay.destroy()
        entry_numplay.destroy()
        button_numplay.destroy()
        window.geometry("400x600")
        display_dice()
        display_game_widgets()
        return num_players



def game_move(x):
    global random_list, score, upper_score_frame, lower_score_frame, dice_frame
    if x == game_buttons[0] or x == game_buttons[1] or x == game_buttons[2] or x == game_buttons[3] or x == game_buttons[4] or x == game_buttons[5]:
        score[x-1] += random_list.count(x)*x
        print("VARIABLE")
    if x == 7:  # Chance Button
        for i in random_list:
            score[6] += i  # it finds the sum of all the values in the randomly generated dice numbers
    if x == 8:  # Yahtzee Button
        if random_list[0] == random_list[1] == random_list[2] == random_list[3] == random_list[4]:
            score[7] += 50
    if x == 9:
        if random_list.count(1) >= 3 or random_list.count(2) >= 3 or random_list.count(3) >= 3 or random_list.count(4) >= 3 or random_list.count(5) >= 3 or random_list.count(6) >= 3:
            for i in random_list:
                score[8] += i
    if x == 10:
        if random_list.count(1) >= 4 or random_list.count(2) >= 4 or random_list.count(3) >= 4 or random_list.count(4) >= 4 or random_list.count(5) >= 4 or random_list.count(6) >= 4:
            for i in random_list:
                score[9] += i
    if x == 11:
        for i in range(6):
            if random_list.count(i) == 3 and (random_list.count((i+1)% 6) == 2 or random_list.count((i+2)% 6) == 2 or random_list.count((i+3)% 6) == 2 or random_list.count((i+4)% 6) == 2 or random_list.count((i+5)% 6) == 2):
                score[10] += 25

    if x == 12:
        if (1 in random_list and 2 in random_list and 3 in random_list and 4 in random_list) or (2 in random_list and 3 in random_list and 4 in random_list and 5 in random_list) or (3 in random_list and 4 in random_list and 5 in random_list and 6 in random_list):
            score[11] += 30
    if x == 13:
        if (1 in random_list and 2 in random_list and 3 in random_list and 4 in random_list and 5 in random_list) or (2 in random_list and 3 in random_list and 4 in random_list and 5 in random_list and 6 in random_list):
            score[12] += 40
    """upper_score_frame.update()
    lower_score_frame.update()
    dice_frame.update()"""


def display_game_widgets():
        for i in range(0, len(game_labels)):
            var = lambda a:game_move(a)
            # Appends the list so that we can display all the widgets at the same time through the iteration of a list
            game_buttons.append(tk.Button(upper_score_frame, text=game_labels[i], command=lambda b=game_labels[-1]: game_move(b)))
            game_scores.append(tk.Label(upper_score_frame, text=score[i], width=2, height=1))

            game_buttons[-1].grid(row=(i+2) if i < 6 else i+5, column=1, sticky="e")
            game_scores[-1].grid(row=(i+2) if i < 6 else i+5, column=3, sticky="w")

            # Make the text appear read only
            game_scores[-1].configure(state="disabled")

        # Current score and bonus award
        upper_score = tk.Text(upper_score_frame, width=2, height=1)
        upper_score.grid(row=8, column=3)
        bonus_score = tk.Text(upper_score_frame, width=2, height=1)
        bonus_score.grid(row=9, column=3)
        bonus_title = tk.Label(upper_score_frame, text="Upper Score: ")
        bonus_title.grid(column=1, row=8)
        upper_title = tk.Label(upper_score_frame, text="Bonus Score: ")
        upper_title.grid(column=1, row=9)
        blank_line = tk.Label(upper_score_frame, text="")
        blank_line.grid(column=1, row=10)
        window.update()


def roll():
    pass

def display_dice():
    global a
    for a in range(0, len(hold_labels)):
        dice_buttons.append(tk.Button(dice_frame, text=hold_labels[a], command=game_move))
        dice_numbers.append(tk.Text(dice_frame, width=4, height=1))

        dice_buttons[-1].grid(row=1, column=a+4, sticky='e')
        dice_numbers[-1].grid(row=2, column=a+4, sticky='w')

    roll_button = tk.Button(dice_frame, text="Roll", command=roll())
    roll_button.grid(row=1, column=10, sticky='n')
    rolls_left = tk.Text(upper_score_frame, width=2, height=1)
    rolls_left.grid(row=2, column=2)

# Obtain the number of players
label_numplay = tk.Label(text="Enter number of players (1-2): ")
label_numplay.grid(column=0, row=2)
entry_numplay = tk.Entry(width=1, bd=2)
entry_numplay.grid(column=1, row=2)

# Confirm number of player button
button_numplay = tk.Button(text="Enter Players", command=confirm_players)
button_numplay.grid(column=3, row=2)

# Reserve space for dice
dice_frame = tk.Label()
dice_frame.grid(columnspan=20, rowspan=3)  # Reserve space for the dice area

# Reserve space for the scores
upper_score_frame = tk.Label()
upper_score_frame.grid(columnspan=3, rowspan=3)  # Reserve space for the upper scores
lower_score_frame = tk.Label()
lower_score_frame.grid(columnspan=3, rowspan=3)  # reserve space for the lower scores



# Display the main window infinitely
window.mainloop()
