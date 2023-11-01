from turtle import Turtle, Screen
from demo21_paddle import Paddle
from demo21_ball import Ball
from demo21_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.title("PING PONG CHING CHONG")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(l_paddle.move_up, "W")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(l_paddle.move_down, "S")

screen.onkey(r_paddle.move_up, "i")
screen.onkey(r_paddle.move_up, "I")
screen.onkey(r_paddle.move_down, "k")
screen.onkey(r_paddle.move_down, "K")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_l_score()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_r_score()


screen.exitonclick()
