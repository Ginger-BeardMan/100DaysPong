from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"P1: {self.p1_score}  P2: {self.p2_score}", align=ALIGNMENT, font=FONT)

    def p1_point(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_point(self):
        self.p2_score += 1
        self.update_scoreboard()
