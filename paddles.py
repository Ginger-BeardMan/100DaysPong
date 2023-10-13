from turtle import Turtle


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape('square')
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        current_y = self.ycor()
        current_y += 20
        self.sety(current_y)

    def move_down(self):
        current_y = self.ycor()
        current_y -= 20
        self.sety(current_y)
