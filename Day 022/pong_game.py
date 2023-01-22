import time
from turtle import Screen

from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("PONG game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle(350, 0)

on_game = True


def quit_game():
    global on_game
    on_game = False


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(quit_game, "q")

while on_game:
    screen.update()
    time.sleep(0.001)

screen.exitonclick()
