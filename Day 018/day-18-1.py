# ####Turtle Intro######

import turtle as t

timmy_the_turtle = t.Turtle()


# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

# ####### Challenge 1 - Draw a Square ############
def l_turn():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


for _ in range(4):
    l_turn()
