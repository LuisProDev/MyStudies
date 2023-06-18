import turtle as t
import random as r

my_screen = t.Screen()
my_screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

user_bet = my_screen.textinput(title="Make your bet",
                               prompt="Which turtle will win? Enter a color: ").lower()

y = -130
for i in range(0, 6):
    y += 40
    turtles = t.Turtle('turtle')
    turtles.color(colors[i])
    turtles.penup()
    turtles.goto(-230, y)
    all_turtles.append(turtles)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won, the winner was the {winner} one")
            else:
                print(f"You lost, the winner was the {winner} one")

        random_dist = r.randint(0, 10)
        turtle.forward(random_dist)


my_screen.exitonclick()