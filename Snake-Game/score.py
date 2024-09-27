from turtle import Turtle

Alignment =  "Center"
Font = ("Arial", 10, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.goto(0 , 270)
        self.hideturtle()
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score}" , move=False, align=Alignment, font=Font)
        self.score += 1

    def game_end(self):
        self.goto(0 , 0 )
        self.write("Game Over" , move= False , align= Alignment , font=Font)
