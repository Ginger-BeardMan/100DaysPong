from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed('slowest')

    def movement(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 7.5
        self.goto(new_x, new_y)
