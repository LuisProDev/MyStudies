from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.actual_y = self.ycor()
        self.actual_x = self.xcor()

    def create_ball(self):
        self.shape('circle')
        self.color('white')
        self.shapesize(1.5)
        self.penup()
        self.speed(1)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def collision(self):
        self.actual_y = self.ycor()
        self.actual_x = self.xcor()
        if self.actual_y >= 180 or self.actual_y <= -180:
            self.actual_y -= 10
            self.actual_x += 10
            self.goto(self.actual_x, self.actual_y)
