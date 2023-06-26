from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def up_key(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def level_up(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()
