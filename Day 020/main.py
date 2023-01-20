import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

snake_body = []


def make_snake_body_init(body: list) -> list:
    pos_x = 0
    for _ in range(3):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.setx(pos_x)
        body.append(t)
        pos_x -= 20

    return body


snake_body: list = make_snake_body_init(snake_body)

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    for i in range(len(snake_body) - 1, 0, -1):
        cords = snake_body[i - 1].pos()
        # print(f"i = {i}, pos = {cords}")
        snake_body[i].setpos(cords)
    snake_body[0].forward(20)

screen.exitonclick()
