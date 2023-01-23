import time
from turtle import Screen

from player import Player
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
game_is_on = True


def quit_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(quit_game, "q")

sleep_timer = 0.1
while game_is_on:
    time.sleep(sleep_timer)
    screen.update()
    if player.is_finished():
        scoreboard.update_score()
        player.start_over()
        sleep_timer *= 0.9

scoreboard.game_over()
screen.exitonclick()
