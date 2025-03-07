import turtle
class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=0.5, stretch_len=8, outline=None)
        self.paddle.color("silver")
        self.paddle.penup()
        self.paddle.goto(0, -290)
        self.paddle.speed(10)
        self.xcor = 1


    def move_left(self):
        self.paddle.setheading(180)  # Face left
        self.paddle.forward(10)
        self.limit()


    def move_right(self):
        self.paddle.setheading(0)  # Face right
        self.paddle.forward(10)
        self.limit()

    def limit(self):
        if self.paddle.xcor() > 270:
            self.paddle.setx(270)
        elif self.paddle.xcor() < -270:
            self.paddle.setx(-270)

