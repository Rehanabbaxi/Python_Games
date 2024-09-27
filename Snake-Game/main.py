from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.tracer(0)



screen.setup(width=600,height=600,startx=0,starty=0)
screen.title("my snake game")
screen.bgcolor("black")


# creating objects of imported classes

snake_obj = Snake()
food_obj = Food()
score_obj = Score()




snake_obj.create_snake()
screen.listen()

screen.onkey(snake_obj.Up, "Up")
screen.onkey(snake_obj.Down, "Down")
screen.onkey(snake_obj.Right, "Right")
screen.onkey(snake_obj.Left, "Left")



game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move()

#     detect collision with food
    if snake_obj.head.distance(food_obj) < 15 :
        food_obj.refresh()
        score_obj.print_score()
        snake_obj.extent_segment()


    #    detect colision with wall
    if snake_obj.head.xcor() > 280 or snake_obj.head.xcor() < -280 or snake_obj.head.ycor() > 280 or snake_obj.head.ycor() < -280 :
        score_obj.game_end()
        game_on = False

    # detect collision  with tail
    for segment in snake_obj.segments[1:]:

        if snake_obj.head.distance(segment) < 10:
            game_on = False
            score_obj.game_end()




screen.exitonclick()