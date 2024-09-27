FONT = ("Courier", 24, "normal")

from  turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200 , 250)
        self.score = 1
        self.show_score()

    def update_score(self):
        self.score +=1

    def show_score(self):
        self.clear()
        self.write(f"Score {self.score} ", align="center", font=FONT)

    def Game_over(self):
        self.goto(0 ,0 )
        self.write("Game Over" ,align="center" , font=FONT)