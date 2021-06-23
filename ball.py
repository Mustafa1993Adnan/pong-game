from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    # moving the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # reflect the ball when hitting the top or bottom wall
    def y_bounce(self):
        self.y_move *= -1
        self.ball_speed *= 0.9
    def x_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
        self.ball_speed = 0.1
