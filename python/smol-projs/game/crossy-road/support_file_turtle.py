from turtle import Turtle

DISTANCE = 20
STARTING_POSITION = (0, -270)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.level_up()

    def move_up(self):
        self.setheading(90)
        self.forward(DISTANCE)

    def move_down(self):
        if self.ycor() > -280:
            self.setheading(270)
            self.forward(DISTANCE)

    def move_right(self):
        if self.xcor() < 240:
            self.setheading(0)
            self.forward(DISTANCE)

    def move_left(self):
        if self.xcor() > -240:
            self.setheading(180)
            self.forward(DISTANCE)

    def level_up(self):
        self.goto(STARTING_POSITION)



