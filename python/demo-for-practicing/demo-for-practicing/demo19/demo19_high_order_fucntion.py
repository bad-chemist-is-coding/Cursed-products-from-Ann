import turtle

screen = turtle.Screen()
ann = turtle.Turtle()


def turn_left():
    new_heading = ann.heading() + 10
    ann.setheading(new_heading)


def turn_right():
    new_heading = ann.heading() - 10
    ann.setheading(new_heading)


def move_forward():
    ann.forward(10)


def move_backward():
    ann.backward(10)


def clear():
    ann.clear()
    ann.penup()
    ann.home()


def lift_pen():
    ann.penup()


def lower_pen():
    ann.pendown()


screen.listen()
# Higher order functions
# screen.onkey() is higher order function because it takes another function as an input
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_left)
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="c", fun=clear)
screen.onkey(key="u", fun=lift_pen)
screen.onkey(key="i", fun=lower_pen)

screen.exitonclick()
