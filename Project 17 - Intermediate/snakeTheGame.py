import turtle as t
from snake import Snake
import random as r
import time

my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title("The snake")
my_screen.tracer(0)

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, key="Up")
my_screen.onkey(snake.down, key="Down")
my_screen.onkey(snake.left, key="Left")
my_screen.onkey(snake.right, key="Right")

while True:
    my_screen.update()
    time.sleep(0.1)
    snake.move()


my_screen.exitonclick()