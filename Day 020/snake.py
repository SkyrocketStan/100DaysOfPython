from turtle import Turtle


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
            pos_x -= 20

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            cords = self.body[i - 1].pos()
            # print(f"i = {i}, pos = {cords}")
            self.body[i].setpos(cords)
        self.body[0].forward(20)
