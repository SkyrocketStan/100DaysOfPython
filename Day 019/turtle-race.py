import random
from turtle import Turtle, Screen

in_game = False

screen = Screen()
screen.title("Turtle race")
screen.setup(width=500, height=400)
end_line = screen.screensize()[0] / 2 + 20

bet_color = screen.textinput(title="Make your bet",
                             prompt="which turtle will win the race? Enter a "
                                    "color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = -120
for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    turtles.append(t)
    t.penup()
    t.goto(x=-230, y=y)
    y += 50

if bet_color:
    in_game = True
win_color = None
while in_game:

    for t in turtles:
        dist = random.randint(1, 10)
        t.fd(dist)
        if t.xcor() >= end_line:
            in_game = False
            win_color = t.pencolor()

win_or_not = "won" if bet_color.lower() == win_color else "lost"
print(f"You've {win_or_not}! The {win_color} turtle is the winner! ")

screen.exitonclick()
