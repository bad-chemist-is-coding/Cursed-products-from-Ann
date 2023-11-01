from turtle import Screen, Turtle
from support_file_turtle import Player
from support_file_cars import Cars
from support_file_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(500, 600)
screen.bgcolor("red")
screen.title("BÉ RÙA DẠO ĐỊA NGỤC")
screen.listen()
screen.tracer(0)

player = Player()
cars = Cars()
score_board = Scoreboard()

game_on = True
while game_on:
    time.sleep(0.03)
    screen.update()
    cars.create_left_cars()
    cars.create_right_cars()
    cars.create_above_cars()
    cars.left_car_moving()
    cars.right_car_moving()
    cars.above_car_moving()
    for car in cars.left_cars:
        if car.distance(player) < 20:
            score_board.reset()
            game_on = False
    for car in cars.right_cars:
        if car.distance(player) < 20:
            score_board.reset()
            game_on = False
    if player.ycor() > 290:
        player.level_up()
        cars.increase_speed()
        score_board.add_score()

    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_up, "w")
    screen.onkey(player.move_down, "Down")
    screen.onkey(player.move_down, "s")
    screen.onkey(player.move_right, "Right")
    screen.onkey(player.move_right, "d")
    screen.onkey(player.move_left, "Left")
    screen.onkey(player.move_left, "a")

screen.exitonclick()
