import time
from turtle import Screen

from food import Food
from snake import Snake

snake = Snake()
food = Food()

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def quit_game():
    global game_over

    game_over = True


screen.onkey(quit_game, "q")
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 15:
        food.refresh()
# screen.exitonclick()
