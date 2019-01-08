# Yahtzee Game Main Program
# Author : Aryan Kinge, Date : December 2018

# Import Libraries
import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the main window title
window.title("Pointless Yahtzee Game")

# Set the main window size in pixels
window.geometry("400x600")

# Ensure that the user cannot resize the window
window.resizable(width=False, height=False)

game_labels = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes"]
game_buttons = []
game_scores = []
random_list = [1, 2, 3, 2, 1]
print(game_scores)
score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Define functions
def confirm_players():
    num_players = entry_numplay.get()
    print(num_players)
    if num_players == "1" or num_players == "2":
        print("Number of players is confirmed as " + num_players)
        label_numplay.destroy()
        entry_numplay.destroy()
        button_numplay.destroy()
        window.geometry("400x600")
        display_game_widgets()
        return num_players



def game_move(x):
    global random_list, score
    print(x)
    if x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6:
        score[x-1] += random_list.count(x)*x
    if x == 7:  # Chance Button
        for i in random_list:
            score[6] += i # it finds the sum of all the values in the randomly generated dice numbers
    """if x == 8:
        score[7] +=
    if x == 9:
    if x == 10:
    if x == 11:
    if x == 12:
    if x == 13:"""
    print(score)


def display_game_widgets():
    for i in range(0, len(game_labels)):

        # Appends the list so that we can display all the widgets at the same time through the iteration of a list
        game_buttons.append(tk.Button(upper_score_frame, text=game_labels[i], command=lambda: game_move(i+1)))
        game_scores.append(tk.Text(upper_score_frame, width=2, height=1))

        game_buttons[-1].grid(row=i+2, column=1, sticky="e")
        game_scores[-1].grid(row=i+2, column=3, sticky="w")

        # Make the text appear read only
        game_scores[-1].configure(state="disabled")

    # butons
    Chance = tk.Button(lower_score_frame, text= "Chance: ", bg="white", command=lambda:game_move(7))
    Chance.grid(row=9, column=1, sticky="e")

    # Current score and bonus award
    upper_score = tk.Text(upper_score_frame, width=2, height=1)
    upper_score.grid(row=i+3, column=3)
    bonus_score = tk.Text(upper_score_frame, width=2, height=1)
    bonus_score.grid(row=i+4, column=3)
    bonus_title = tk.Label(upper_score_frame, text="Upper Score: ")
    bonus_title.grid(column=1, row=i+3)
    upper_title = tk.Label(upper_score_frame, text="Upper Score: ")
    upper_title.grid(column=1, row=i+4)
    blank_line = tk.Label(upper_score_frame, text="")
    blank_line.grid(column=1, row=i+5)
    window.update()


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
dice_frame.grid(columnspan=8, rowspan=3)  # Reserve space for the dice area

# Reserve space for the scores
upper_score_frame = tk.Label()
upper_score_frame.grid(columnspan=3, rowspan=3)  # Reserve space for the upper scores
lower_score_frame = tk.Label()
lower_score_frame.grid(columnspan=3, rowspan=3)  # reserve space for the lower scores

print(game_scores)

# Display the main window infinitely
window.mainloop()
