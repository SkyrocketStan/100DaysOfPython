from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("classic")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.left(90)
        self.goto(start_pos)

    def move(self):
        if -1000 < self.ycor() < 1000:
            self.goto(self.xcor(), (self.ycor() + 10))


class ShipBullet(Bullet):
    def __init__(self, start_pos):
        super().__init__(start_pos)


class EnemyBullet(Bullet):
    def __init__(self, start_pos):
        super().__init__(start_pos)
        self.left(180)

    def move(self):
        if -1000 < self.ycor() < 1000:
            self.goto(self.xcor(), (self.ycor() - 5))
