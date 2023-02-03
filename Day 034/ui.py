from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizUI:
    def __init__(self):
        self.score_label = None
        self.image_no = None
        self.image_yes = None
        self.window = Tk()
        self.canvas = None
        self.button_no = None
        self.button_yes = None

        self.get_window()
        self.get_canvas()
        self.get_buttons()
        self.get_scoreboard()

        self.window.mainloop()

    def get_scoreboard(self):
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

    def get_buttons(self):
        self.image_yes = PhotoImage(file="images/true.png")
        self.image_no = PhotoImage(file="images/false.png")
        self.button_yes = Button(image=self.image_yes, highlightthickness=0)
        self.button_no = Button(image=self.image_no, highlightthickness=0)
        self.button_yes.grid(row=2, column=1)
        self.button_no.grid(row=2, column=0)

    def get_window(self):
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

    def get_canvas(self):
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Some quiz text", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
