from turtle import Turtle
import random

COLORS = ["black", "blue", "green", "yellow", "pink", "orange", "purple"]
CAR_MOVING_SPEED = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        self.left_cars = []
        self.right_cars = []
        self.above_cars = []
        self.car_speed = CAR_MOVING_SPEED

    def create_left_cars(self):
        random_spawning = random.randint(1, 8)
        if random_spawning == 8:
            new_left_cars = Turtle("square")
            new_left_cars.penup()
            new_left_cars.shapesize(1, 2)
            new_left_cars.color(random.choice(COLORS))
            rand_y_cor = random.randint(-250, 250)
            new_left_cars.goto(x=-250, y=rand_y_cor)
            self.left_cars.append(new_left_cars)

    def create_right_cars(self):
        random_spawning = random.randint(1,8)
        if random_spawning == 8:
            new_right_cars = Turtle("square")
            new_right_cars.penup()
            new_right_cars.shapesize(1,2)
            new_right_cars.color(random.choice(COLORS))
            rand_y_cor_r = random.randint(-250, 250)
            new_right_cars.goto(250, rand_y_cor_r)
            self.right_cars.append(new_right_cars)

    def create_above_cars(self):
        random_spawning = random.randint(1, 10)
        if random_spawning == 8:
            new_above_cars = Turtle("square")
            new_above_cars.setheading(270)
            new_above_cars.penup()
            new_above_cars.shapesize(1, 2)
            new_above_cars.color(random.choice(COLORS))
            rand_x_cor = random.randint(-220, 220)
            new_above_cars.goto(rand_x_cor, 300)
            self.left_cars.append(new_above_cars)

    def left_car_moving(self):
        for cars in self.left_cars:
            cars.forward(self.car_speed)

    def right_car_moving(self):
        for cars in self.right_cars:
            cars.backward(self.car_speed)

    def above_car_moving(self):
        for cars in self.above_cars:
            cars.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



