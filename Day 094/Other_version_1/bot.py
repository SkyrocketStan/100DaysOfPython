# bot.py
from turtle import Turtle
from shot import EnemyBullet


class Bot(Turtle):
    def __init__(self, start_pos, shape):
        super().__init__()
        self.penup()
        self.color((58, 227, 32))
        self.shape(shape)
        self.goto(start_pos)
        self.speed = 5
        self.bullets = []
        self.points = 5

    def move(self):
        self.goto((self.xcor() + self.speed), self.ycor())

    def check(self):
        if self.xcor() > 280 or self.xcor() < -280:
            return True

    def down(self):
        self.speed *= -1
        self.goto((self.xcor() + self.speed), (self.ycor() - 20))

    def shoot(self):
        new_bullet = EnemyBullet((self.xcor(), self.ycor()))
        self.bullets.append(new_bullet)


class Mothership(Bot):
    def __init__(self, start_pos):
        super().__init__(start_pos, "turtle")
        self.points = 100
        self.shapesize(stretch_wid=1.65, stretch_len=1.65)
        self.speed = 5
        # self.left(90)
