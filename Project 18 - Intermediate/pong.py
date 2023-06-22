import turtle as t
from pads import Pads
from ball import Ball
from score import Score
import time

my_screen = t.Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor('black')
my_screen.title('Pong')
my_screen.tracer(0)
my_screen.listen()

player_one = Pads(-350, 0)
player_two = Pads(350, 0)
ball = Ball()
score = Score()

my_screen.onkeypress(player_one.up_key, key='w')
my_screen.onkeypress(player_one.down_key, key='s')
my_screen.onkeypress(player_two.up_key, key='Up')
my_screen.onkeypress(player_two.down_key, key='Down')

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(player_two) < 50 and ball.xcor() > 320 \
            or ball.distance(player_one) < 50 and ball.xcor() < -320:
        ball.pad_bounce()

    if ball.xcor() > 380:
        score.p_two_score()
        ball.reset_ball()

    if ball.xcor() < -380:
        score.p_one_score()
        ball.reset_ball()

my_screen.exitonclick()
