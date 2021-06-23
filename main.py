from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle(position=(370, 0))
l_paddle = Paddle(position=(-370, 0))

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.paddle_go_up, "Up")
screen.onkeypress(r_paddle.paddle_go_down, "Down")

screen.onkeypress(l_paddle.paddle_go_up, "w")
screen.onkeypress(l_paddle.paddle_go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detect the collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
