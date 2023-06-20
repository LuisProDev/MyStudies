import turtle as t
import snake
import food
import score
import time

# Screen setup
my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title("The snake")
my_screen.tracer(0)

# Objects
snake = snake.Snake()
food = food.Food()
score = score.Score()

# Movement of the snake
my_screen.listen()
my_screen.onkey(snake.up, key="Up")
my_screen.onkey(snake.down, key="Down")
my_screen.onkey(snake.left, key="Left")
my_screen.onkey(snake.right, key="Right")

game_is_on = True
# Game loop
while game_is_on:
    my_screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.wall_collision():
        game_is_on = False
        score.game_over()

    # Collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.track_points()


my_screen.exitonclick()