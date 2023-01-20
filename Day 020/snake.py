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

    # self.snake_body: list = self.make_snake_body_init()

    # def make_snake_body_init(self) -> list:
    #     pos_x = 0
    #     body = []
    #     for _ in range(3):
    #         t = Turtle("square")
    #         t.color("white")
    #         t.penup()
    #         t.setx(pos_x)
    #         body.append(t)
    #         pos_x -= 20
    #
    #     return body

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            cords = self.body[i - 1].pos()
            # print(f"i = {i}, pos = {cords}")
            self.body[i].setpos(cords)
        self.body[0].forward(20)
    # def move(self):
    #     for i in range(len(self.snake_body) - 1, 0, -1):
    #         cords = self.snake_body[i - 1].pos()
    #         # print(f"i = {i}, pos = {cords}")
    #         self.snake_body[i].setpos(cords)
    #     self.snake_body[0].forward(20)
