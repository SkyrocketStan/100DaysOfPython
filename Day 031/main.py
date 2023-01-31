import random
import tkinter as tk
from tkinter import messagebox

import pandas

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_IMAGE_FILE = "images/card_back.png"
CARD_FRONT_IMAGE_FILE = "images/card_front.png"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
DATA_FILE_CSV = "data/french_words.csv"
FLIP_CARD_TIMER_MS = 1000


def read_data():
    try:
        data_fame = pandas.read_csv(DATA_FILE_CSV)
    except FileNotFoundError:
        messagebox.showerror("Datafile unreachable",
                             f"Data file {DATA_FILE_CSV} cannot be read.")
        exit(1)
    return data_fame


def get_words_dict() -> list:
    data = read_data()
    dict_list = data.to_dict(orient="records")
    return dict_list


words_list = get_words_dict()
current_card = {}


def update_card():
    global current_card
    current_card = random.choice(words_list)


def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    update_card()
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(FLIP_CARD_TIMER_MS, flip_card_to_en)


def flip_card_to_en():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = tk.Tk()
window.title("Flash cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(height=526, width=800, highlightthickness=0,
                   bg=BACKGROUND_COLOR)
card_front_img = tk.PhotoImage(file=CARD_FRONT_IMAGE_FILE)
card_back_img = tk.PhotoImage(file=CARD_BACK_IMAGE_FILE)

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
flip_timer = window.after(1, next_card)

canvas.grid(row=0, column=0, columnspan=2)

ok_image = tk.PhotoImage(file="images/right.png")
ok_button = tk.Button(image=ok_image, highlightthickness=0,
                      command=next_card)
ok_button.grid(row=1, column=1)

x_image = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_image, highlightthickness=0)
x_button.grid(row=1, column=0)

window.mainloop()
