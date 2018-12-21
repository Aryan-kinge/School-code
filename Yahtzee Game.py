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
dice_frame.grid(columnspan=0, rowspan=3)

# Reserve space for the scores


# Display the main window infinitely
window.mainloop()
