import turtle as t
from random import randint

tim = t.Turtle()
t.colormode(255)

########### Challenge 3 - Draw Shapes ########

for angles in range(4, 9):
    angle = 360 / angles
    print(angle)
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))

    for _ in range(angles):
        tim.fd(100)
        tim.right(angle)
