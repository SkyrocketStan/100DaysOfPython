import random
import tkinter as tk
from tkinter import messagebox

import pandas

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK = "images/card_front.png"
CARD_FRONT = "images/card_back.png"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
DATA_FILE = "data/french_words.csv"


def read_data():
    try:
        data_fame = pandas.read_csv(DATA_FILE)
    except FileNotFoundError:
        messagebox.showerror("Datafile unreachable",
                             f"Data file {DATA_FILE} cannot be read.")
        exit(1)
    return data_fame


def get_words_dict() -> list:
    data = read_data()
    dict_list = data.to_dict(orient="records")
    return dict_list


words_list = get_words_dict()


def get_random_word():
    a_dict = random.choice(words_list)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=a_dict["French"])


window = tk.Tk()
window.title("Flash cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(height=526, width=800, highlightthickness=0,
                   bg=BACKGROUND_COLOR)
card_image = tk.PhotoImage(file=CARD_FRONT)
canvas.create_image(400, 263, image=card_image)
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
get_random_word()

canvas.grid(row=0, column=0, columnspan=2)

ok_image = tk.PhotoImage(file="images/right.png")
ok_button = tk.Button(image=ok_image, highlightthickness=0,
                      command=get_random_word)
ok_button.grid(row=1, column=1)

x_image = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_image, highlightthickness=0)
x_button.grid(row=1, column=0)

window.mainloop()
