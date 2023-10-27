import time
from turtle import Turtle, Screen

ann = Turtle()
showing_screen = Screen()
showing_screen.addshape('smiley.gif')
showing_screen.addshape('drunk.gif')
showing_screen.addshape('vomit.gif')
showing_screen.addshape('sleep.gif')
showing_screen.bgpic('background.gif')
showing_screen.title('Chu trình của người say')
showing_screen.textinput("BẠN CÓ SAY KHÔNG?", "Bạn có tỉnh không?")


def go_drinking():
    ann.shape('smiley.gif')
    time.sleep(1)
    ann.penup()
    ann.speed(1)
    ann.forward(200)
    ann.left(90)
    ann.forward(100)
    ann.left(60)


def getting_drunk():
    ann.shape('drunk.gif')
    ann.speed(1)
    i = 0
    while i < 10:
        ann.forward(50)
        ann.left(30)
        ann.forward(50)
        ann.right(30)
        i += 2
    ann.back(100)
    time.sleep(1)


def vomit():
    ann.shape('vomit.gif')
    ann.pendown()
    ann.color('green')
    i = 0
    while i < 20:
        ann.speed(100)
        ann.circle(20)
        ann.left(20)
        i += 1
    ann.penup()
    ann.speed(1)
    ann.forward(100)


def go_to_bed():
    ann.shape('drunk.gif')
    ann.left(100)
    i = 0
    while i < 10:
        ann.forward(50)
        ann.left(30)
        ann.forward(50)
        ann.right(30)
        i += 2
    time.sleep(0.5)
    ann.shape('sleep.gif')


go_drinking()
getting_drunk()
vomit()
go_to_bed()

print(ann)
print(showing_screen)
showing_screen.exitonclick()
