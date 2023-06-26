from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.points = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-280, 260)
        self.write(arg=f'Level:{self.points + 1}', font=FONT)

    def update_score(self):
        self.points += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",
                   align='center',
                   font=('Courier', 12, "normal"))