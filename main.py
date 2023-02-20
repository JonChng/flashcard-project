from tkinter import *
import pandas as pd
from random import choice
from pathlib import Path
import time

BACKGROUND_COLOR = "#B1DDC6"
filepath = Path('data/words_to_learn.csv')

try:
    words = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    words = pd.read_csv("data/french_words.csv")

list_of_words = list(words.to_dict(orient="records"))
words_to_learn = []
current_card = {"French":"Ready?", "English":"Click to start!"}

def right():
    global list_of_words, current_card

    list_of_words.remove(current_card)

def wrong_ans():
    global current_card, words_to_learn

    words_to_learn.append(current_card)
    df = pd.DataFrame(words_to_learn)
    df.to_csv(filepath, index=False)

def change_card():
    global current_card,flip_timer

    window.after_cancel(flip_timer)
    current_card = choice(list_of_words)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card['French'])
    canvas.itemconfig(image, image=card_front)
    flip_timer = window.after(3000, func=flip)

def flip():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"])
    canvas.itemconfig(image, image=card_back)


# UI CREATION
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
tick = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")


canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, anchor=CENTER, image=card_front)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text=current_card["French"], font=("Arial", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=tick, highlightthickness=0, command=lambda:[change_card(), right()])
right_button.config(highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=lambda:[change_card(), wrong_ans()])
wrong_button.config(highlightthickness=0)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(3000, func=flip)

window.mainloop()

