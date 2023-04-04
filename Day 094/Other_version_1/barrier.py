# barrier.py
from turtle import Turtle


class BarrierPiece(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.goto(start_pos)
        self.color((58, 227, 32))


class Barrier:
    def __init__(self, x, y):
        self.blocks = []
        self.x = x
        self.y = y
        for i in range(0, 40):
            new_block = BarrierPiece((self.x + i, self.y))
            self.blocks.append(new_block)
