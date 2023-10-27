import time
from turtle import Screen, Turtle
from support_file_snake import Snake, Enermy, Bomb
from support_file_food import Food
from support_file_scoreboard import Score_board

screen = Screen()
screen.setup(600, 600)
screen.title("BÉ NA CHƠI VỚI BÉ RÙA")
screen.bgcolor("black")
mode = screen.textinput("CHỌN ĐỘ KHÓ", "(A) Chế độ Dễ: Chơi như bình thường\n"
                                "(B) Chế độ Trung bình: Bé Rùa bị tăng động\n(C) Chế độ Khó: Bé Rùa tăng động dưới mưa\n"
                                       "(D) Chế độ Asian: Bé Rùa tăng động dưới mưa ở khu có bom").lower()

screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score_board = Score_board()

if mode == "d":
    bombs = []
    for _ in range(1, 11):
        bomb = Bomb()
        bombs.append(bomb)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.moving()
    if mode == "b":
        food.moving_food()
    if mode == "c":
        rain = Enermy()
        food.moving_food()
    if mode == "d":
        rain = Enermy()
        food.moving_food()
        for bomb in bombs:
            if snake.head.distance(bomb) < 20:
                game_on = False
                score_board.game_over()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow_body()
        score_board.add_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() < -290 or snake.head.ycor() > 300:
        game_on = False
        score_board.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()

    screen.onkey(snake.move_up, "W")
    screen.onkey(snake.move_down, "S")
    screen.onkey(snake.move_right, "D")
    screen.onkey(snake.move_left, "A")
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "s")
    screen.onkey(snake.move_right, "d")
    screen.onkey(snake.move_left, "a")

screen.exitonclick()
