import turtle
from ball import Ball
from barriers import Barriers


class GamePlay:
    def __init__(self):
        self.ball = Ball()
        self.barrier = Barriers()
        self.paddle = turtle.Turtle()

        # Level barriers
        self.level1_1, self.level1_2 = self.barrier.level_1()
        self.level2_1, self.level2_2 = self.barrier.level_2()
        self.level3_1, self.level3_2 = self.barrier.level_3()
        self.level4_1, self.level4_2 = self.barrier.level_4()

        self.main_barrier = self.barrier.main_barrier()
        self.sub_main_barriers = self.barrier.mgb
        self.main_barrier_hits = 0

    def ball_movement(self):
        self.ball.movement()

    def ball_hits_wall(self):

        if self.ball.ycor() > 295:
            self.ball.bounce_y()
        elif abs(self.ball.xcor()) > 345:
            self.ball.bounce_x()
        elif abs(self.ball.ycor() < -295):
            self.ball.bounce_y()

    def ball_hits_mgb(self):

        for mgb_barrier in self.sub_main_barriers:
            if self.ball.distance(mgb_barrier) < 20:
                self.ball.bounce_y()
                self.sub_main_barriers.remove(mgb_barrier)
                self.increase_speed(0.0025)

    def ball_hits_main_barrier(self):
        if self.ball.distance(self.main_barrier) < 20:
            self.ball.bounce_y()
            self.main_barrier_hits += 1
            self.increase_speed(0.005)

            # Break the barrier after 5 hits
            if self.main_barrier_hits >= 5:
                self.main_barrier.hideturtle()

    def check_collision(self, level_blocks):
        for block in level_blocks[::-1]:
            if self.ball.distance(block) < 20:
                self.ball.bounce_y()
                self.increase_speed(0.0015)


    def level1_collision(self):
        self.check_collision(self.level1_1)
        self.check_collision(self.level1_2)

    def level2_collision(self):
        self.check_collision(self.level2_1)
        self.check_collision(self.level2_2)

    def level3_collision(self):
        self.check_collision(self.level3_1)
        self.check_collision(self.level3_2)

    def level4_collision(self):
        self.check_collision(self.level4_1)
        self.check_collision(self.level4_2)

    def increase_speed(self, percentage):
        self.ball.move_speed *= (1 + percentage)

