import turtle
import random
import colorgram

# HOW TO USE THIS SHIT: SCROLL DOWN TO TYPEABLE PLACE AND FOLLOW THE INSTRUCTIONS

# SKIP THIS COLOR GENERATOR
rgb_colors = []
colors = colorgram.extract('bleeding_eyes.png', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)

# DON'T TOUCH CODES BELOW
ann = turtle.Turtle()
turtle.colormode(255)
ann.speed(0)
ann.penup()
ann.hideturtle()
ann.setheading(215)
ann.forward(300)
ann.setheading(0)
number_of_dots = 100


# SOME COLOR PALETTES NAMES
# DON'T TOUCH CODES BELOW
def pastel():
    color_list = [(244, 227, 206), (200, 225, 242), (245, 196, 218), (226, 167, 192), (176, 171, 202), (193, 212, 167),
                  (164, 213, 212), (197, 218, 202), (163, 213, 215), (191, 168, 197), (177, 176, 208)]
    for dot_count in range(1, number_of_dots + 1):
        ann.dot(50, random.choice(color_list))
        ann.forward(50)
        if dot_count % 10 == 0:
            ann.setheading(90)
            ann.forward(50)
            ann.setheading(180)
            ann.forward(500)
            ann.setheading(0)


def blues():
    color_list = [(7, 44, 55), (83, 188, 229), (188, 231, 244), (22, 119, 154), (29, 165, 214), (234, 250, 248),
                  (136, 209, 236), (16, 83, 105)]
    for dot_count in range(1, number_of_dots + 1):
        ann.dot(50, random.choice(color_list))
        ann.forward(50)
        if dot_count % 10 == 0:
            ann.setheading(90)
            ann.forward(50)
            ann.setheading(180)
            ann.forward(500)
            ann.setheading(0)


def greys():
    color_list = [(158, 158, 158), (55, 55, 55), (91, 91, 91), (238, 238, 238)]
    for dot_count in range(1, number_of_dots + 1):
        ann.dot(50, random.choice(color_list))
        ann.forward(50)
        if dot_count % 10 == 0:
            ann.setheading(90)
            ann.forward(50)
            ann.setheading(180)
            ann.forward(500)
            ann.setheading(0)


def bleeding_eyes():  # Beware of destroying your eyes
    color_list = [(255, 0, 0), (93, 0, 255), (255, 0, 232), (255, 250, 0), (0, 248, 255)]
    for dot_count in range(1, number_of_dots + 1):
        ann.dot(50, random.choice(color_list))
        ann.forward(50)
        if dot_count % 10 == 0:
            ann.setheading(90)
            ann.forward(50)
            ann.setheading(180)
            ann.forward(500)
            ann.setheading(0)


# TYPE BELOW A NAME OF PALETTES ABOVE TO COLOR THE BALLS
bleeding_eyes()

# DON'T TOUCH CODES BELOW
screen = turtle.Screen()
screen.exitonclick()
