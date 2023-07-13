import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.up_key, key='w')
car_manager = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car) < 20 and player.xcor() <= car.xcor():
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        player.level_up()
        car_manager.increase_speed()
        score.update_score()

screen.exitonclick()

