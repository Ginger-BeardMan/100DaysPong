from turtle import Screen, Turtle
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

net = Turtle()
screen = Screen()
r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

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
    ball.movement()
    # scoreboard.player_score()

    # ball collision with wall
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce_y()

    # ball collision with paddles
    if ball.distance(r_paddle) < 40 and ball.xcor() >= 330 or ball.distance(l_paddle) < 40 and ball.xcor() <= -330:
        ball.bounce_x()

        if ball.x_move > 0:
            ball.x_move += 5
        elif ball.x_move < 0:
            ball.x_move -= 5

    # score and resetting the ball
    if ball.xcor() > 370:
        ball.player_miss()
        ball.x_move = -10
        scoreboard.p1_point()
    elif ball.xcor() < -370:
        ball.player_miss()
        ball.x_move = 10
        scoreboard.p2_point()


screen.exitonclick()
