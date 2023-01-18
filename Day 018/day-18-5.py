import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########
screen = t.Screen()
tim.speed(0)

for _ in range(36):
    tim.color(random_color())
    tim.circle(100)
    tim.right(10)

screen.exitonclick()
