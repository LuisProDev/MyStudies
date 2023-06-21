import turtle as t
from pads import Pads
import time

my_screen = t.Screen()
my_screen.setup(width=1000, height=500)
my_screen.bgcolor('black')
my_screen.title('Pong')
my_screen.tracer(0)
my_screen.listen()

player_one = Pads(-480, 0)
player_two = Pads(475, 0)

my_screen.onkeypress(player_one.up_key, key='w')
my_screen.onkeypress(player_one.down_key, key='s')
my_screen.onkeypress(player_two.up_key, key='Up')
my_screen.onkeypress(player_two.down_key, key='Down')

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.02)

my_screen.exitonclick()
