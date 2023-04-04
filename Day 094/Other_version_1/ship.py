# ship.py
from turtle import Turtle
from shot import ShipBullet

Y = -250


class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color((58, 227, 32))
        self.shape("turtle")
        self.goto(0, Y)
        self.left(90)
        self.bullets = []
        self.speed = 15

    def move_left(self):
        if self.xcor() > -280:
            self.goto((self.xcor() - self.speed), Y)

    def move_right(self):
        if self.xcor() < 280:
            self.goto((self.xcor() + self.speed), Y)

    def shoot(self):
        current_bullet = ShipBullet((self.xcor(), self.ycor()))
        self.bullets.append(current_bullet)
