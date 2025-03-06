import turtle



class Barriers:
    def __init__(self):
        self.main_turtle = None
        self.mgb = []
        self.level1_list1 = []
        self.level1_list2 = []
        self.level2_list1 = []
        self.level2_list2 = []
        self.level3_list1 = []
        self.level3_list2 = []
        self.level4_list1 = []
        self.level4_list2 = []

    def main_barrier(self):
        self.main_turtle = turtle.Turtle()
        self.main_turtle.penup()
        self.main_turtle.speed(0)
        self.main_turtle.shape("square")
        self.main_turtle.color("#F8F3D9")
        self.main_turtle.turtlesize(stretch_wid=2, stretch_len=35, outline=None)
        self.main_turtle.goto(0, 260)
        return self.main_turtle

    def main_gide_barriers(self):
        self.mgb = [turtle.Turtle() for i in range(6)]
        n = -267.14
        for i, t in enumerate(self.mgb):
            t.speed(0)
            t.penup()
            t.color("#F8F3D9")
            t.shape("square")
            t.shapesize(stretch_wid=3, stretch_len=2)
            self.mgb[i].goto(x=n, y=230)
            n += 102.85

    def level_barrier(self, turtle_color, l1_y, l2_y, level_list1, level_list2):

        list1 = [turtle.Turtle() for i in range(35)]
        n = -340
        for i, t in enumerate(list1):
            t.hideturtle()
            t.speed(0)
            t.penup()
            t.pencolor("black")
            t.fillcolor(turtle_color)
            t.begin_fill()
            t.shape("square")
            t.shapesize(stretch_wid=1, stretch_len=1)
            t.goto(n, l1_y)
            t.end_fill()
            t.showturtle()
            n += 20
            level_list1.append(t)

        list2 = [turtle.Turtle() for i in range(35)]
        n = -340
        for i, j in enumerate(list2):
            j.hideturtle()
            j.speed(0)
            j.penup()
            j.pencolor("black")
            j.fillcolor(turtle_color)
            j.begin_fill()
            j.shape("square")
            j.shapesize(stretch_wid=1, stretch_len=1)
            j.goto(n, l2_y)
            j.end_fill()
            j.showturtle()
            n += 20
            level_list2.append(j)

    def level_4(self):
        self.level_barrier(turtle_color="red", l1_y=180, l2_y=160, level_list1=self.level4_list1,
                           level_list2=self.level4_list2)
        return self.level4_list1, self.level4_list2

    def level_3(self):
        self.level_barrier(turtle_color="orange", l1_y=140, l2_y=120, level_list1=self.level3_list1,
                           level_list2=self.level3_list2)
        return self.level3_list1, self.level3_list2

    def level_2(self):
        self.level_barrier(turtle_color="green", l1_y=100, l2_y=80, level_list1=self.level2_list1,
                           level_list2=self.level2_list2)
        return self.level2_list1, self.level2_list2

    def level_1(self):
        self.level_barrier(turtle_color="yellow", l1_y=60, l2_y=40, level_list1=self.level1_list1,
                           level_list2=self.level1_list2)
        return self.level1_list1, self.level1_list2
