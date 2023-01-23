from turtle import Turtle

FONT = ("Courier", 24, "normal")
TEXT_ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self, x_pos=-200, y_pos=250):
        super().__init__()
        self.score = 1
        self.color("black")
        self.setpos(x_pos, y_pos)
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.update_text()

    def update_score(self):
        self.score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align=TEXT_ALIGN,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=TEXT_ALIGN, font=FONT)
