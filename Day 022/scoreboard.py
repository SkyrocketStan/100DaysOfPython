from turtle import Turtle

TEXT_ALIGN = "center"
TEXT_FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self, y_pos=200):
        super().__init__()
        self.l_score = 0
        self.r_score = 0

        self.color("white")
        self.setpos(0, y_pos)
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.update_text()

    def update_score(self, paddle: str):
        if paddle.lower() == 'l':
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", move=False,
                   align=TEXT_ALIGN,
                   font=TEXT_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=TEXT_ALIGN,
                   font=TEXT_FONT)
