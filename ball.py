from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def movement(self):
        x_coordinate = self.xcor() + self.x_cor
        y_coordinate = self.ycor() + self.y_cor
        self.goto(x_coordinate, y_coordinate)

    def bounce_y(self):
        self.y_cor *= -1

    def bounce_x(self):
        self.x_cor *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
