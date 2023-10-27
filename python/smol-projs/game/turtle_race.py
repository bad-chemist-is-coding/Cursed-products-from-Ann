from turtle import Screen, Turtle
import random

game_start = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Đoán rùa thắng",
                            "Có 6 bé rùa đua với nhau tên:\nYellow, Red, Green, Blue, Orange, Purple\nNhập tên bé rùa bạn nghĩ sẽ thắng:").lower()
colors = ["yellow", "red", "green", "blue", "orange", "purple"]
all_turtles = []
vertical_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=vertical_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    game_start = True
while game_start:
    for turtle in all_turtles:
        winning_color = turtle.pencolor()
        if turtle.xcor() > 220:
            game_start = False
            if user_bet == winning_color:
                print(f"🟩 Chúc mừng bạn đã thắng cược! 🥳\n🐢Bạn nên cảm ơn bé {user_bet}!🐢")
            else:
                print(
                    f"🟥 Ôi không, không may bé {winning_color} đã thắng mất rồi 😧\n💀 Bạn nên thịt bé {user_bet} đi là vừa 💀")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
