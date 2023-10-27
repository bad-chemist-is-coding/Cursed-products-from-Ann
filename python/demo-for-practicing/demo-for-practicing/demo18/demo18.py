import turtle
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('pastel.jpg',12)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
turtle.colormode(255)
ann = turtle.Turtle()
color_list = [(244, 227, 206), (200, 225, 242), (245, 196, 218), (226, 167, 192), (176, 171, 202), (193, 212, 167), (164, 213, 212), (197, 218, 202), (163, 213, 215), (191, 168, 197), (177, 176, 208)]

ann.speed(0)
ann.penup()
ann.hideturtle()
ann.setheading(215)
ann.forward(300)
ann.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    ann.dot(50, random.choice(color_list))
    ann.forward(50)
    if dot_count % 10 == 0:
        ann.setheading(90)
        ann.forward(50)
        ann.setheading(180)
        ann.forward(500)
        ann.setheading(0)

screen = turtle.Screen()
screen.exitonclick()