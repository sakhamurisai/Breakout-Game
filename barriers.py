import turtle
from turtle import *


class Barriers:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle_list = []
        self.level_list1 = []
        self.level_list2 = []

    def main_barrier(self):
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color("#F8F3D9")
        self.turtle.turtlesize(stretch_wid=2, stretch_len=35, outline=None)
        self.turtle.goto(0, 260)

    def main_gide_barriers(self):
        self.turtle_list = [turtle.Turtle() for i in range(6)]
        n = -267.14
        for i, t in enumerate(self.turtle_list):
            t.speed(0)
            t.penup()
            t.color("#F8F3D9")
            t.shape("square")
            t.shapesize(stretch_wid=3, stretch_len=2)
            self.turtle_list[i].goto(x=n, y=230)
            n += 102.85

    def level_barrier(self, turtle_color, l1_y, l2_y):
        self.level_list1 = [turtle.Turtle() for i in range(70)]
        n = -350
        for i, t in enumerate(self.level_list1):
            t.speed(0)
            t.penup()
            t.pencolor("black")
            t.fillcolor(turtle_color)
            t.begin_fill()
            t.shape("square")
            t.shapesize(stretch_wid=0.5, stretch_len=0.5)
            t.goto(n, l1_y)
            t.end_fill()
            n += 10

        self.level_list2 = [turtle.Turtle() for i in range(70)]
        n = -350
        for i, t in enumerate(self.level_list2):
            t.speed(0)
            t.penup()
            t.pencolor("black")
            t.fillcolor(turtle_color)
            t.begin_fill()
            t.shape("square")
            t.shapesize(stretch_wid=0.5, stretch_len=0.5)
            t.goto(n, l2_y)
            t.end_fill()
            n += 10

    def level_4(self):
        self.level_barrier(turtle_color="red", l1_y=190,l2_y=180)

    def level_3(self):
        self.level_barrier(turtle_color="orange", l1_y=170,l2_y=160)

    def level_2(self):
        self.level_barrier(turtle_color="green", l1_y=150,l2_y=140)

    def level_1(self):
        self.level_barrier(turtle_color="yellow", l1_y=130,l2_y=120)
