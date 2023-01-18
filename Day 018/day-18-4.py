import random
import turtle as t

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

screen = t.Screen()
tim.speed(0)
tim.pensize(15)

for _ in range(50):
    tim.color(random.choice(colours))
    tim.fd(50)
    tim.setheading(random.choice([0, 90, 180, 270]))

screen.exitonclick()
