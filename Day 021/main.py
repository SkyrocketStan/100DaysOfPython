import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

EATING_DISTANCE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

snake = Snake()
food = Food()
score = Scoreboard()

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

screen_border_positive_x = SCREEN_WIDTH / 2 - EATING_DISTANCE
screen_border_negative_x = -1 * screen_border_positive_x

screen_border_positive_y = SCREEN_HEIGHT / 2 - EATING_DISTANCE
screen_border_negative_y = -1 * screen_border_positive_y


def quit_game():
    global game_over
    game_over = True


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(quit_game, "q")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= EATING_DISTANCE:
        food.refresh()
        score.update_score()

    if snake.head.xcor() > screen_border_positive_x or snake.head.xcor() < \
            screen_border_negative_x or snake.head.ycor() > \
            screen_border_positive_y or snake.head.ycor() < \
            screen_border_negative_y:
        score.game_over()
        game_over = True

screen.exitonclick()
