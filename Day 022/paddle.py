from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__("square")
        self.color("white")
        p_width = HEIGHT // WIDTH
        p_len = WIDTH // 20  # 20 is a default square size
        self.shapesize(stretch_wid=p_width, stretch_len=p_len)
        self.penup()
        self.goto(x_pos, y_pos)

    def up(self):
        self.goto(self.xcor(), self.ycor() + WIDTH)

    def down(self):
        self.goto(self.xcor(), self.ycor() - WIDTH)
