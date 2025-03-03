import turtle
from turtle import Screen
from barriers import Barriers
from play import GamePlay

screen = Screen()
screen.setup(width=700,height=600)
screen.bgcolor("black")
screen.delay(0)
screen.listen()

barrier = Barriers()
gameplay = GamePlay()
barrier.main_barrier()
barrier.main_gide_barriers()
barrier.level_4()
barrier.level_3()
barrier.level_2()
barrier.level_1()
left = gameplay.move_left()
right = gameplay.move_right()
screen.onkey(left,"Left")
screen.onkey(right,"Right")
game_on = True
while game_on:
    screen.update()
    gameplay.ball_movement()
    gameplay.ball_hits_wall()
    gameplay.level1_collision()
    gameplay.level2_collision()
    gameplay.level3_collision()
    gameplay.level4_collision()
    gameplay.ball_hits_mgb()
    gameplay.ball_hits_main_barrier()
    gameplay.paddle_play()


