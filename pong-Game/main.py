from turtle import Screen
from padle import Padle
from ball import Ball
from score import  Score
import time


screen_obj = Screen()
screen_obj.setup(width= 800 , height= 600)
screen_obj.bgcolor("Black")
screen_obj.tracer(0)


# instantiating classes
l_padle = Padle((350,0))
r_padle = Padle((-350 , 0))
ball = Ball()
score = Score()

screen_obj.listen()

screen_obj.onkey(l_padle.move_up , "Up")
screen_obj.onkey(l_padle.move_down , "Down")

screen_obj.onkey(r_padle.move_up , "w")
screen_obj.onkey(r_padle.move_down , "s")


game_on = True
while game_on:
    time.sleep(ball.sp)
    screen_obj.update()
    ball.move()

    #  detecting uppar wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #     detect paddle collision
    if ball.distance(l_padle) < 50 and ball.xcor() > 330 or ball.distance(r_padle) < 50 and ball.xcor() <-330:
        ball.bounce_x()


    #   detect ball missed paddle collision  on right side
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #   detect ball missing collision on left sid paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen_obj.exitonclick()