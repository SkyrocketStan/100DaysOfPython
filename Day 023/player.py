from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
WIDTH = 20


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_finished(self):
        return True if self.ycor() >= FINISH_LINE_Y else False

    def start_over(self):
        self.goto(STARTING_POSITION)
