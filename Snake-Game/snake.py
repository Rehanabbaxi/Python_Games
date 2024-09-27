Positions = [(0,0) , (-20,0) , (-40 ,0)]
move_distance = 20
from turtle import Turtle
up = 90
down = 270
left = 180
right = 0

class Snake():

    def __init__(self ):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in Positions:
            self.add_segment(position)


    def add_segment(self ,  position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        # tim.goto(Positions[position])
        tim.goto(position)
        self.segments.append(tim)

    def extent_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self ):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)

        self.segments[0].forward(move_distance)


    def Up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def  Down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def  Left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def  Right(self):
        if self.head.heading() != left:
            self.head.setheading(right)