from turtle import Turtle, Screen
import random
import turtle as t

# from turtle import * # used to import many classes from 1 module, but easy to get confused. Should avoid
# import turtle as t # if not using from...import..., wew can replace the module name turtle as t
ann = Turtle()
ann.shape("turtle")
ann.color("yellow")
ann.pencolor("red")


# ann.forward(100)
# ann.left(90)
#
# for _ in range(3):
#     ann.forward(100)
#     ann.left(90)
# ann.right(90)
# for _ in range(15):
#     ann.forward(10)
#     ann.penup()
#     ann.forward(10)
#     ann.pendown()
# ann.right(180)
# ann.forward(300)

colors = ["red", "pink", "yellow", "blue", "green", "purple", "orange"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         ann.forward(100)
#         ann.right(angle)
#
#
# for shape_side_n in range(3,11):
#     ann.color(random.choice(colors))
#     draw_shape(shape_side_n)
#
# screen = Screen()
# screen.exitonclick()


directions = [0, 90, 180, 270]


ann.pensize(15)
ann.speed(0)
for _ in range(200):
    ann.color(random.choice(colors))
    ann.forward(30)
    ann.setheading(random.choice(directions))



ann = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    ran_color = (r, g, b)
    return ran_color


direction = [0, 90, 180, 270]
ann.pensize(15)
ann.speed(3)

for _ in range(200):
    ann.color(random_color())
    ann.forward(30)
    ann.setheading(random.choice(direction))
