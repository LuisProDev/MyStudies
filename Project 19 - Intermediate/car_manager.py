from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.starting_speed = 5

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(290, random.randint(-200, 280))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.starting_speed)

    def increase_speed(self):
        self.starting_speed += MOVE_INCREMENT
