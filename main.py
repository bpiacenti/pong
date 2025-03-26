from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


ball = Ball()
paddleR = Paddle((350, 0))
paddleL = Paddle((-350, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=paddleR.pad_up, key="Up")
screen.onkeypress(fun=paddleL.pad_up, key="w")
# screen.onkeyrelease(fun=pad_up_release, key="Up")
screen.onkeypress(fun=paddleR.pad_down, key="Down")
screen.onkeypress(fun=paddleL.pad_down, key="s")
# screen.onkeyrelease(fun=pad_down_release, key="Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddleR) < 50 and ball.xcor() > 320 or ball.distance(paddleL) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.right_point()

screen.exitonclick()