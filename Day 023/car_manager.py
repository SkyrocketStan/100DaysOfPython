import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, width, height):

        super().__init__()
        self.hideturtle()
        self.cars = []
        self.screen_width = width
        self.screen_height = height
        self.move_distance = STARTING_MOVE_DISTANCE
        self.right_edge = (self.screen_width // 2)
        self.left_edge = self.right_edge * -1

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # new_car.move_distance = STARTING_MOVE_DISTANCE
            # new_car.right_edge = (self.width // 2)
            # new_car.left_edge = self.right_edge * -1
            # new_car.height = self.height
            self.go_random_start_pos(new_car)
            self.cars.append(new_car)

    def go_random_start_pos(self, car):
        # self.color(random.choice(COLORS))
        car.goto(self.random_pos())

    def random_pos(self):
        high_y = (self.screen_height // 2) - 50
        low_y = high_y * -1
        y_pos = random.randint(low_y, high_y)
        x_pos = self.right_edge - 20
        return x_pos, y_pos

    def move_cars(self):
        for car in self.cars:
            if car.xcor() <= self.left_edge:
                self.go_random_start_pos(car)
            else:
                car.backward(self.move_distance)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
