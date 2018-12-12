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

# Obtain the number of players
laberl_numplay = tk.Label(text="Enter number of players (1-2): ")
label_numplay.grid(column=0, row=2)

# Display the main window infinitely
window.mainloop()
