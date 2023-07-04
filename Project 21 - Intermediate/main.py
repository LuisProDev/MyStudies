import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("U.S States Game")
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)

# while True:
guess = turtle.textinput("Guess", "Guess a State")
states = pandas.read_csv("50_states.csv")
guess_row = states[states.state == guess]
x_location = guess_row.x
y_location = guess_row.y
print(x_location)


my_screen.mainloop()
