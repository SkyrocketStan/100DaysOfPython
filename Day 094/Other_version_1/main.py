from turtle import Screen
import time
from ship import Ship
from bot import Bot, Mothership
from scoreboard import Scoreboard
import random
from barrier import Barrier

screen = Screen()
screen.colormode(255)
screen.setup(width=610, height=600)
screen.title("Space Invaders")
screen.tracer(0)
screen.bgcolor("black")
game_on = True

BARRIER_Y = -200

# life1 = Ship()
# life2 = Ship()
# life3 = Ship()

lives = [Ship(), Ship(), Ship()]

ship = lives[0]
screen.listen()
screen.onkey(ship.move_left, "Left")
screen.onkey(ship.move_right, "Right")
screen.onkey(ship.shoot, "space")

bots = []
active_bullets = []
shapes = ["square", "circle", "arrow", "classic", "triangle", "square", "circle", "arrow", "classic", "triangle",
          "square", "circle", "arrow", "classic", "triangle"]
row = 0

sb = Scoreboard()

barriers = [Barrier(-200, BARRIER_Y), Barrier(-50, BARRIER_Y), Barrier(100, BARRIER_Y)]


# Functions
def lose_life():
    global game_on, lives, ship
    for bullet in ship.bullets:
        bullet.goto(1000, 1000)
        bullet.hideturtle()
        ship.bullets = []

    if len(lives) == 1:
        sb.game_over()
        game_on = False
    else:
        lives[0].goto(1000, 1000)
        lives[0].hideturtle()
        lives.remove(lives[0])
        ship = lives[0]
        ship.goto(0, -250)
        screen.onkey(ship.move_left, "Left")
        screen.onkey(ship.move_right, "Right")
        screen.onkey(ship.shoot, "space")


def restart():
    global bots, active_bullets, shapes, row, ship, lives

    for i in range(0, len(lives)):
        lives[i].goto(-300 + (i * 30), -270)

    ship = lives[0]

    for bot in bots:
        bot.goto(1000, 1000)
        bot.hideturtle()

    bots = []

    for b in active_bullets:
        b.goto(1000, 1000)
        b.hideturtle()

    for s in ship.bullets:
        s.goto(1000, 1000)
        s.hideturtle()

    active_bullets = []
    ship.bullets = []
    row = 0
    for i in range(-250, 220, 40):
        for j in range(100, 200, 40):
            new_bot = Bot((i, j), shape=shapes[row])
            bots.append(new_bot)
            row += 1
        row = 0
    ship.goto(0, -250)
    sb.write_score()


start_time = round(time.time(), 1)


def check_bar(bullet_list):
    r_index = []

    for barrier in barriers:
        for block in barrier.blocks:
            for shot in bullet_list:
                if block.distance(shot) < 20:
                    block.goto(1000, 1000)
                    block.hideturtle()
                    r_index.append([barriers.index(barrier), block])
                    shot.goto(1000, 1000)
                    shot.hideturtle()
                    break

    for r in r_index:
        barriers[r[0]].blocks.remove(r[1])


restart()
ms_active = False
mother_ship = Mothership((-500, -500))
while game_on:
    screen.update()
    time.sleep(0.01)

    if round(time.time()) - start_time > 45:
        ms_active = True
        mother_ship.goto((-300, 250))
        start_time = time.time()

    for bot in bots:
        if bot.check():
            for xbot in bots:
                xbot.down()
        bot.move()

    for shot in ship.bullets:
        shot.move()
        if shot.distance(mother_ship) < 20:
            shot.goto(1000, 1000)
            shot.hideturtle()
            ship.bullets.remove(shot)
            mother_ship.goto(1000, 1000)

        for bot in bots:
            if shot.distance(bot) < 20:
                bot.goto(1000, 1000)
                bot.hideturtle()
                bots.remove(bot)
                shot.goto(1000, 1000)
                shot.hideturtle()
                ship.bullets.remove(shot)
                sb.score += bot.points
                sb.write_score()

    for bot in bots:
        if bot.ycor() <= BARRIER_Y:
            lose_life()
            # sb.game_over()
            # game_on = False

    for bot in bots:
        shoot = random.randint(0, 200)
        if shoot == 0:
            bot.shoot()
        for shot in bot.bullets:
            active_bullets.append(shot)

    for bullet in active_bullets:
        bullet.move()
        if bullet.distance(ship) < 15:
            # sb.game_over()
            # game_on = False
            lose_life()

    if not bots:
        sb.level_up()
        lives = [Ship(), Ship(), Ship()]
        ship.goto(1000, 1000)
        ship.hideturtle()
        ship = lives[0]
        restart()
        screen.update()
    check_bar(active_bullets)
    check_bar(ship.bullets)

    if ms_active:
        mother_ship.move()

screen.exitonclick()

