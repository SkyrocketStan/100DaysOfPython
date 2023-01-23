import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.title("Turtle race")

player = Player()
scoreboard = Scoreboard()
game_is_on = True


def quit_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(quit_game, "q")

car_manager = CarManager(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

sleep_timer = 0.1
while game_is_on:
    time.sleep(sleep_timer)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()
    if player.is_finished():
        scoreboard.update_score()
        player.start_over()
        car_manager.speed_up()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            quit_game()

scoreboard.game_over()
screen.exitonclick()
