from tkinter import *
from ui import Buttons

BUTTON_BG_COLOR = "#2B2B2B"
BUTTON_FG_COLOR = "#FAF7F0"
BG_COLOR = "#000000"
OPERATOR_FG_COLOR = "#000000"

# Window setup
window = Tk()
window.title("Basic Calculator")
window.config(padx=20, pady=10, bg=BG_COLOR)
window.minsize(width=300, height=300)
user_entry = ""


# Taking user input from button
def on_click(text):
    entry.insert(entry.index(INSERT), text)


# Calculation function
def plus(num1, num2):
    result = num1 + num2
    entry.delete(0, END)
    entry.insert(0, string=result)


def minus(num1, num2):
    result = num1 - num2
    entry.delete(0, END)
    entry.insert(0, string=result)


def mul(num1, num2):
    result = num1 * num2
    entry.delete(0, END)
    entry.insert(0, string=result)


def div(num1, num2):
    result = num1 / num2
    entry.delete(0, END)
    entry.insert(0, string=result)


# Error handling
def invalid_occurrence():
    entry.delete(0, END)
    entry.insert(0, string="Invalid input")


# Reset function
def reset_entry():
    global user_entry
    user_entry = user_entry.replace(user_entry, "")
    entry.delete(0, END)


# Calculate function for taking user input and go through each char and calculate function calling for calculation
def calculate():
    global user_entry
    user_entry += entry.get()

    for char in user_entry:
        if char == "+" or char == "-" or char == "*" or char == "/":
            num1 = int(user_entry[:user_entry.index(char)])
            num2 = int(user_entry[user_entry.index(char) + 1:])
            if char == "+":
                plus(num1, num2)
            elif char == "-":
                minus(num1, num2)
            elif char == "*":
                mul(num1, num2)
            elif char == "/":
                div(num1, num2)
            else:
                invalid_occurrence()


# Entry

entry = Entry()
entry.grid(column=1, row=0, pady=30)
entry.focus()

# Button
ac_button = Buttons("AC", 2, 4, bg_color="#D6E4E5", command=reset_entry, fg=OPERATOR_FG_COLOR)
button_0 = Buttons("0", 3, 4, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("0"), fg=BUTTON_FG_COLOR)
button_1 = Buttons("1", 2, 3, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("1"), fg=BUTTON_FG_COLOR)
button_2 = Buttons("2", 3, 3, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("2"), fg=BUTTON_FG_COLOR)
button_3 = Buttons("3", 4, 3, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("3"), fg=BUTTON_FG_COLOR)
button_4 = Buttons("4", 2, 2, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("4"), fg=BUTTON_FG_COLOR)
button_5 = Buttons("5", 3, 2, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("5"), fg=BUTTON_FG_COLOR)
button_6 = Buttons("6", 4, 2, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("6"), fg=BUTTON_FG_COLOR)
button_7 = Buttons("7", 2, 1, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("7"), fg=BUTTON_FG_COLOR)
button_8 = Buttons("8", 3, 1, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("8"), fg=BUTTON_FG_COLOR)
button_9 = Buttons("9", 4, 1, bg_color=BUTTON_BG_COLOR, command=lambda: on_click("9"), fg=BUTTON_FG_COLOR)

# Operator buttons
plus_button = Buttons("+", 1, 1, bg_color="#EEEEEE", command=lambda: on_click("+"), fg=OPERATOR_FG_COLOR)
minus_button = Buttons("-", 1, 2, bg_color="#EEEEEE", command=lambda: on_click("-"), fg=OPERATOR_FG_COLOR)
multiplication_button = Buttons("*", 1, 3, bg_color="#EEEEEE", command=lambda: on_click("*"), fg=OPERATOR_FG_COLOR)
division_button = Buttons("/", 1, 4, bg_color="#EEEEEE", command=lambda: on_click("/"), fg=OPERATOR_FG_COLOR)

equal_button = Buttons("=", 4, 4, bg_color="#EEEEEE", command=calculate, fg=OPERATOR_FG_COLOR)

window.mainloop()
