import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK = "images/card_front.png"
CARD_FRONT = "images/card_back.png"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

window = tk.Tk()
window.title("Flash cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(height=526, width=800, highlightthickness=0,
                   bg=BACKGROUND_COLOR)
card_image = tk.PhotoImage(file=CARD_FRONT)
canvas.create_image(400, 263, image=card_image)
canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
canvas.create_text(400, 263, text="Word", font=WORD_FONT)

canvas.grid(row=0, column=0, columnspan=2)

ok_image = tk.PhotoImage(file="images/right.png")
ok_button = tk.Button(image=ok_image, highlightthickness=0)
ok_button.grid(row=1, column=1)

x_image = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_image, highlightthickness=0)
x_button.grid(row=1, column=0)

window.mainloop()
