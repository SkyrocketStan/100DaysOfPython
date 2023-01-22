import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WALL_DISTANCE = 30

r_paddle_x = (SCREEN_WIDTH // 2) - WALL_DISTANCE
l_paddle_x = r_paddle_x * -1

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("PONG game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle(r_paddle_x, 0)
left_paddle = Paddle(l_paddle_x, 0)

ball = Ball()

on_game = True


def quit_game():
    global on_game
    on_game = False


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(quit_game, "q")

screen_ceiling = SCREEN_HEIGHT // 2 - WALL_DISTANCE
screen_floor = SCREEN_HEIGHT // -2 + WALL_DISTANCE
while on_game:
    screen.update()
    ball.move()
    time.sleep(0.1)
    if ball.ycor() >= screen_ceiling or ball.ycor() <= screen_floor:
        ball.bounce_y()

    if ball.xcor() >= (r_paddle_x - 20) and ball.distance(right_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() <= (l_paddle_x + 20):
        ball.bounce_x()

screen.exitonclick()
