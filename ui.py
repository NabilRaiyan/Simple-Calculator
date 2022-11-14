from tkinter import *

FONT = ("Courier", 16, "bold")


# Button

class Buttons:
    def __init__(self, name, column, row, bg_color, command, fg):
        self.button = Button(text=name, font=FONT, bg=bg_color, command=command, fg=fg)
        self.button.config(padx=15, pady=5)
        self.button.grid(column=column, row=row, padx=5, pady=5)
        self.user_input = self.button.cget("text")
