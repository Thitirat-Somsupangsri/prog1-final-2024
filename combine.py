import turtle
import random


class ball:
    def __init__(self):
        self.num_ball = 5
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.canvas_width = turtle.screensize()[0]
        ball_radius = 0.05 * self.canvas_width
        self.canvas_height = turtle.screensize()[1]
        self.size = ball_radius
        self.x = random.uniform(-1*self.canvas_width + ball_radius, self.canvas_width - ball_radius)
        self.y = random.uniform(-1*self.canvas_height + ball_radius, self.canvas_height - ball_radius)


    def draw_ball(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def

class five_ball(ball):
    def __init__(self):
        super().__init__()

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

class number:
    def __init__(self):