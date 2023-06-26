from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(random.randint())
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=0.5, stretch_len=2.5)