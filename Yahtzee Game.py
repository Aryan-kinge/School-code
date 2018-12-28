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

game_labels = [0, 1, 2, 3, 4, 5, 6 ]
game_buttons = []
game_scores = []

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
        return num_players

def display_game_widgets():
    for i in range(0, len(game_labels)):
        game_buttons.append(tk.Button(upper_score_frame, text=game_labels[i], command=game_move))
        game_scores.append(tk.Text(upper_score_frame, width=2, height=1))

        game_buttons[-1].grid(row=i+2, column=1, sticky="e")
        game_scores[-1].grid(row=i+2, column=3, sticky="w")

        # Make the text appear read only
        game_scores[-1].configure(state="disabled")

    # Current score and bonus award
    upper_score = tk.Text(upper_score_frame, width=2, height=1)
    upper_score.grid(row=i+3, column=3)
    bonus_score = tk.Text(upper_score_frame, width=2, height=1)
    bonus_score.grid(row=i+4, column=3)
    bonus_title = tk.Label(upper_score_frame, text="Upper SCore: ")
    bonus_title.grid(column=1, row=i+3)
    upper_title = tk.Label(upper_score_frame, text="Upper SCore: ")
    upper_title.grid(column=1, row=i+4)
    blank_line = tk.Label(upper_score_frame, text="")
    blank_line.grid(column=1, row=i+5)


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
dice_frame.grid(columnspan=0, rowspan=3) # Reserve space for the dice area

# Reserve space for the scores
upper_score_frame = tk.Label()
upper_score_frame.grid(columnspan=3, rowspan=3) # Reserve space for the upper scores
lower_score_frame = tk.Label()
lower_score_frame.grid(columnspan=3, rowspan=3) # reserve space for the lower scores

# Display the main window infinitely
window.mainloop()
