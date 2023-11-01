from turtle import Turtle

DISTANCE = 20
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed("fastest")
        # self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x, y)
        # self.showturtle()
    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - DISTANCE
            self.goto(self.xcor(), new_y)

