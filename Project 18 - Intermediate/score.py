from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player_one_points = 0
        self.player_two_points = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.player_one_points, align='center', font=('Courier', 80, 'normal'))
        self.goto(110, 180)
        self.write(self.player_two_points, align='center', font=('Courier', 80, 'normal'))

    def p_one_score(self):
        self.player_one_points += 1
        self.update()

    def p_two_score(self):
        self.player_two_points += 1
        self.update()