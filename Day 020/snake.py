from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        pos_x = 0
        self.body = []
        for _ in range(3):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.setx(pos_x)
            self.body.append(t)
            pos_x -= DISTANCE
        self.head = self.body[0]
        # self.head.setheading(270)
        # turtle.mode("standard")

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            cords = self.body[i - 1].pos()
            # print(f"i = {i}, pos = {cords}")
            self.body[i].setpos(cords)
        self.body[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
