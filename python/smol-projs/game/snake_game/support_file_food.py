from turtle import Turtle
import random
import time

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
MOVE_SPEED = 20


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.penup()
        self.speed("fastest")
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)


    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

    def moving_food(self):
        directions = [UP, DOWN, LEFT, RIGHT]

        for direction in directions:
            direction = random.choice(directions)
            if self.xcor() < -300:
                self.setheading(RIGHT)
                self.forward(20)
            elif self.xcor() > 290:
                self.setheading(LEFT)
                self.forward(20)
            elif self.ycor() > 300:
                self.setheading(DOWN)
                self.forward(20)
            elif self.ycor() < -290:
                self.setheading(UP)
                self.forward(20)
            self.setheading(direction)
            self.forward(MOVE_SPEED)
