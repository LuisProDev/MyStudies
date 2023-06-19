import turtle as t
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.full_snake = []
        self.x = 0
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for i in range(1, 4):
            turtles = t.Turtle('square')
            turtles.color('white')
            turtles.penup()
            turtles.goto(self.x, 0)
            self.x -= 20
            self.full_snake.append(turtles)

    def move(self):
        for last_snake in range(len(self.full_snake) - 1, 0, -1):
            new_x = self.full_snake[last_snake - 1].xcor()
            new_y = self.full_snake[last_snake - 1].ycor()
            self.full_snake[last_snake].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

