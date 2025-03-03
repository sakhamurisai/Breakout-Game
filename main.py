import turtle
from ball import Ball
from turtle import Screen
from barriers import Barriers

screen = Screen()
screen.setup(width=700,height=600)
screen.bgcolor("black")
screen.delay(0)
barrier = Barriers()
ball = Ball()
barrier.main_barrier()
barrier.main_gide_barriers()
barrier.level_4()
barrier.level_3()
barrier.level_2()
barrier.level_1()
game_on = True
while game_on:
    screen.update()
    ball.movement()
    if ball.ycor() > 295:
        ball.bounce_y()
    elif abs(ball.xcor()) > 345:
        ball.bounce_x()
    elif abs(ball.xcor()) > 345:
        ball.bounce_x()
