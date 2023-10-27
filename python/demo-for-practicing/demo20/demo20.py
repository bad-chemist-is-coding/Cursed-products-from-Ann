from turtle import Turtle, Screen
from demo20_snake import Snake
from demo20_food import Food
from demo20_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Bé Na đi ăn")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.growing_body()
        score.add_score()
    snake.move()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() < -290 or snake.head.ycor() > 300:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_down, "s")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_right, "Right")
    screen.onkey(snake.move_right, "d")




screen.exitonclick()