from turtle import Turtle
import random
import time

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segment.append(new_snake)

    def grow_body(self):
        self.add_segment(self.segment[-1].position())

    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)

    def moving(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


class Enermy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.25, 0.25)
        self.penup()
        self.speed("fastest")
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

class Bomb(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(2, 2)
        self.penup()
        self.speed("fastest")
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)