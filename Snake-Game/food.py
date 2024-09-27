import random
from turtle import Turtle , Screen

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len= 0.5 , stretch_wid= 0.2)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cord = random.randint(-280 , 280)
        y_cord = random.randint(-280 , 280)
        self.goto(x_cord , y_cord)