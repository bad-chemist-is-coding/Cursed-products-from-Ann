import turtle as t
import random

ann = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    ran_color = (r, g, b)
    return ran_color


ann.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        ann.color(random_color())
        ann.circle(100)
        ann.setheading(ann.heading() + 10)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
