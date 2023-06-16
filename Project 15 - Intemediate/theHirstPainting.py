import random
import turtle as t

my_turtle = t.Turtle()
my_turtle.hideturtle()
t.colormode(255)
my_turtle.speed(20)

colors = [(34, 108, 167), (245, 77, 36), (112, 163, 211),
          (153, 57, 85), (219, 156, 94), (201, 60, 27),
          (24, 133, 55), (246, 204, 84), (190, 151, 47),
          (225, 119, 152), (46, 53, 121), (221, 68, 97),
          (113, 199, 156), (147, 37, 30), (253, 202, 0),
          (91, 113, 192), (74, 40, 32), (248, 153, 143),
          (111, 41, 49), (155, 212, 203), (53, 174, 163),
          (38, 31, 67), (154, 210, 219), (43, 33, 45),
          (35, 55, 46), (99, 93, 2), (43, 151, 190),
          (10, 111, 51), (228, 169, 182), (177, 186, 217)]

my_turtle.penup()

my_turtle.setposition(-355.0, -258.0)

for i in range(0, 10):
    y = my_turtle.ycor()
    for j in range(0, 10):
        my_turtle.pendown()
        my_turtle.color(random.choice(colors))
        my_turtle.begin_fill()
        my_turtle.circle(15)
        my_turtle.end_fill()
        my_turtle.penup()
        my_turtle.forward(70)
    my_turtle.setposition(-355, y + 60)


my_screen = t.Screen()
my_screen.exitonclick()










