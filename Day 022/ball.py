from turtle import Turtle

MOVE_STEP = 10
DEF_MOVE_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = MOVE_STEP
        self.y_move = MOVE_STEP
        self.move_speed = DEF_MOVE_SPEED

        # self.setheading(random.randint(0, 360))
        # self.goto(x_pos, y_pos)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.forward(MOVE_STEP)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def new_round(self):
        self.setpos(0, 0)
        self.move_speed = DEF_MOVE_SPEED
        self.bounce_x()
