from turtle import Turtle

class Padle(Turtle):
    def __init__(self, cordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(cordinates)

    def move_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
