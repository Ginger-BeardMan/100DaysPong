from turtle import Screen, Turtle
from paddles import Paddles
from ball import Ball
import time

net = Turtle()
screen = Screen()
r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
pong_ball = Ball()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.tracer(0)

net.hideturtle()
net.speed('fastest')
net.color('white')
net.penup()
net.goto(0, -290)
net.pendown()
net.setheading(90)
net.pensize(2)

for dash in range(26):
    net.forward(15)
    net.penup()
    net.forward(9)
    net.pendown()

screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')

screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    pong_ball.movement()

screen.exitonclick()
