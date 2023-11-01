from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        with open("support_file_highscore_record.txt") as data:
            self.highest_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-230, 220)
        self.write(f"Địa ngục tầng: {self.score}\n Tầng địa ngục sâu nhất từng đến: {self.highest_score}", align="left", font=("Courier", 14, "bold"))

    def add_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Địa ngục tầng: {self.score}\n Tầng địa ngục sâu nhất từng đến: {self.highest_score}", align="left",
                   font=("Courier", 14, "bold"))

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.write("BÉ RÙA ĐÃ LÊN THIÊN ĐÀNG\nVÌ KHÔNG XUỐNG ĐƯỢC ĐỊA NGỤC", align="center", font=("Courier", 15, "bold"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("support_file_highscore_record.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
            self.score = 0
            self.update_score()
        self.game_over()



