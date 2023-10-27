from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Số bé Rùa bé Na đã ăn: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Số bé Rùa bé Na đã ăn: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"Bé Na đã cook!", align=ALIGNMENT, font=FONT)