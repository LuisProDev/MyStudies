from turtle import *
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Pads(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_pads(x, y)

    def create_pads(self, x, y):
        self.shape('square')
        self.penup()
        self.goto(x, y)
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def up_key(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_key(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)