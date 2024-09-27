import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# instantiating imported classes
turtle = Player()
Car_manager_obj = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(turtle.move , "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    Car_manager_obj.create_car()
    Car_manager_obj.move_car()
    score_board.show_score()

# detect colllision with car
    for car  in Car_manager_obj.all_cars:
        if car.distance(turtle) < 20 :
            score_board.Game_over()
            game_is_on = False

    if turtle.is_on_finish():
        turtle.go_to_start()
        Car_manager_obj.level_up()
        score_board.update_score()


screen.exitonclick()