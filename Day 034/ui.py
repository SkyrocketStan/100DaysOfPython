from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.canvas: Canvas = Canvas()
        self.score_label = Label()
        self.question_text = None
        self.image_no = None
        self.image_yes = None
        self.button_no = Button()
        self.button_yes = Button()

        self.set_window()
        self.get_canvas()
        self.set_buttons()
        self.set_scoreboard()

        self.get_next_question()
        self.window.mainloop()

    def set_scoreboard(self):
        self.score_label.config(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

    def set_buttons(self):
        self.image_yes = PhotoImage(file="images/true.png")
        self.image_no = PhotoImage(file="images/false.png")
        self.button_yes.config(image=self.image_yes, highlightthickness=0,
                               command=self.yes_pressed)
        self.button_no.config(image=self.image_no, highlightthickness=0,
                              command=self.no_pressed)
        self.button_yes.grid(row=2, column=1)
        self.button_no.grid(row=2, column=0)

    def set_window(self):
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

    def get_canvas(self):
        # self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.config(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280,
            text="Some quiz text", fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def get_next_question(self):
        self.canvas.config(bg="white")

        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text,
                                   text="No more questions")
            self.button_yes.config(state="disabled")
            self.button_no.config(state="disabled")
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

    def yes_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def no_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        color = "green" if is_right else "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)
