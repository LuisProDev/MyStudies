import time
import turtle as t
import snake as s
import score as sc
import food as f

# Screen setup
my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title("The snake")
my_screen.tracer(0)

# Objects
snake = s.Snake()
food = f.Food()
score = sc.Score()

# Movement of the snake
my_screen.listen()
my_screen.onkey(snake.up, key="Up")
my_screen.onkey(snake.down, key="Down")
my_screen.onkey(snake.lefts, key="Left")
my_screen.onkey(snake.rights, key="Right")

game_is_on = True
# Game loop
while game_is_on:
    # Animation of the screen and Snake
    my_screen.update()
    time.sleep(0.07)
    snake.move()

    # Collision with walls
    if snake.wall_collision():
        score.reset_score()
        snake.reset_snake()

    # Collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.increase_snake()

    # Collision with body
    for squares in snake.full_snake[1:]:
        if snake.head.distance(squares) < 10:
            score.reset_score()
            snake.reset_snake()

my_screen.exitonclick()



