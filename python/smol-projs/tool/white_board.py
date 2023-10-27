import turtle

screen = turtle.Screen()
ann = turtle.Turtle()
ann.pensize(5)


# Move ver/hor: W S D A
# Move forward/backward, turn left/right: Arrows
# Clear: C
# Lift/Lower pen: U/I
# Eraser Mode/Pen Mode: E/R

def move_right():
    ann.pensize(5)
    ann.setheading(0)
    ann.forward(10)


def move_left():
    ann.pensize(5)
    ann.setheading(180)
    ann.forward(10)


def move_up():
    ann.pensize(5)
    ann.setheading(90)
    ann.forward(10)


def move_down():
    ann.pensize(5)
    ann.setheading(270)
    ann.forward(10)


def turn_left():
    ann.pensize(5)
    new_heading = ann.heading() + 10
    ann.setheading(new_heading)


def turn_right():
    ann.pensize(5)
    new_heading = ann.heading() - 10
    ann.setheading(new_heading)


def move_forward():
    ann.pensize(5)
    ann.forward(10)


def move_backward():
    ann.pensize(5)
    ann.backward(10)


def clear():
    ann.clear()
    ann.penup()
    ann.home()


def lift_pen():
    ann.fillcolor("green")
    ann.penup()


def lower_pen():
    ann.pensize(5)
    ann.fillcolor("black")
    ann.pendown()


def eraser_mode():
    ann.pencolor("white")
    ann.fillcolor("red")
    ann.pensize(15)


def pen_mode():
    ann.pensize(5)
    ann.color("black")
    ann.pensize(1)


screen.listen()
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="c", fun=clear)
screen.onkey(key="u", fun=lift_pen)
screen.onkey(key="i", fun=lower_pen)
screen.onkey(key="e", fun=eraser_mode)
screen.onkey(key="r", fun=pen_mode)
screen.exitonclick()
