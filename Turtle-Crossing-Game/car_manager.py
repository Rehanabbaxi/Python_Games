COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_no = random.randint(0,6)
        if random_no == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.goto(280, random.randint(-250, 250))
            new_car.shapesize(stretch_wid = 0.5, stretch_len=1)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)


    def level_up(self):
        self.speed += MOVE_INCREMENT

