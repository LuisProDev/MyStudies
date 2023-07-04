import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("U.S States Game")

image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
score = 0
correct_guesses = []
all_states = states.state.to_list()

while len(correct_guesses) < 50:
    guess = turtle.textinput(f"{score}/50 States Correct", "Guess a State").title()
    if guess == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_states = pandas.DataFrame(missing_states)
        new_states.to_csv("states_to_learn.csv")
        exit()

    elif guess in states["state"].unique():
        score += 1
        guess_row = states[states.state == guess]
        x_location = guess_row.iloc[0]["x"]
        y_location = guess_row.iloc[0]["y"]
        my_state = turtle.Turtle()
        my_state.penup()
        my_state.hideturtle()
        my_state.goto(x_location, y_location)
        my_state.write(arg=f"{guess}", font=("Courier", 6, "normal"))
        correct_guesses.append(guess)
    else:
        continue

my_screen.mainloop()
