from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.go_to_start()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor() ,new_y)

    def is_on_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else :
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)











