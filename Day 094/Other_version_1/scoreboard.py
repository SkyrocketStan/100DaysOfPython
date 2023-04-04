# scoreboard.py
from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.color("white")
        self.level = 1
        self.write_score()

    def write_score(self):
        self.pendown()
        self.clear()
        self.write(f"Level: {self.level}. Score: {self.score}.", move=False, align="center",
                   font=("Courier", 14, "normal"))
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Courier", 20, "normal"))

    def level_up(self):
        self.goto(0, 0)
        self.level += 1
        self.write(f"Level Up: {self.level}", move=False, align="center", font=("Courier", 20, "normal"))
        time.sleep(3)
        self.clear()
        self.penup()
        self.goto(0, 280)
