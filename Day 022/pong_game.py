from turtle import Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("PONG game")
screen.bgcolor("black")

screen.exitonclick()
