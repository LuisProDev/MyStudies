from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(arg=f'Score: {self.points}',
                   move=False, align='center',
                   font=('Courier', 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",
                   align='center',
                   font=('Courier', 12, "normal"))

    def track_points(self):
        self.points += 1
        self.clear()
        self.write(arg=f'Score: {self.points}',
                   move=False, align='center',
                   font=('Courier', 12, "normal"))


