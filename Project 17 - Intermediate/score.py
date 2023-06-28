from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("score.txt") as score:
            self.high_score = int(score.read())
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(arg=f'Score: {self.points} '
                       f'High Score: {self.high_score}',
                   move=False, align='center',
                   font=('Courier', 12, "normal"))

    def reset_score(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("score.txt", "w+") as score:
                score.write(str(self.high_score))
        self.points = 0
        self.track_points()

    def track_points(self):
        self.clear()
        self.write(arg=f'Score: {self.points}'
                       f' High Score: {self.high_score}',
                   move=False, align='center',
                   font=('Courier', 12, "normal"))

    def increase(self):
        self.points += 1
        self.track_points()