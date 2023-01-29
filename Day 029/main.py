# PASSWORD GENERATOR
from tkinter import *

# SAVE PASSWORD

# UI SETUP
window = Tk()
window.title("Password manager")
window.config(pady=20, padx=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.pack()

window.mainloop()
