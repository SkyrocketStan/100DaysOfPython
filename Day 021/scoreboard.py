from turtle import Turtle

TEXT_ALIGN = "center"
TEXT_FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.setpos(0, 250)
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.update_text()

    def update_score(self):
        self.score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Score {self.score}", move=False, align=TEXT_ALIGN,
                   font=TEXT_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=TEXT_ALIGN,
                   font=TEXT_FONT)
