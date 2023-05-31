import random
import time
import os

def guessing_game():
    def guess():
        if difficulty == 'easy':
            for i in range(10,0, -1):
                time.sleep(0.5)
                print(f"You have {i} attempts left")
                guess_easy = int(input("Make a guess: "))
                if guess_easy > random_number:
                    print("Too high!")
                    print("Guess again.")
                elif random_number > guess_easy:
                    print("Too low!")
                    print("Guess again.")
                elif guess_easy == random_number:
                    print(f"Exact number! The answer was {guess_easy}")  
        if difficulty == 'hard':
            for i in range(5,0, -1):
                time.sleep(0.5)
                print(f"You have {i} attempts left")
                guess_hard = int(input("Make a guess: "))
                if guess_hard > random_number:
                    print("Too high!")
                    print("Guess again.")
                elif random_number > guess_hard:
                    print("Too low!")
                    print("Guess again.")
                elif guess_hard == random_number:
                    print(f"Exact number! The answer was {guess_hard}")   
        print("You've run out of guesses, you lose") 

    print("Welcome to the Number Guessing Game!")
    time.sleep(1)
    print("I'm thinking of a number between 1 and 100.")
    time.sleep(1)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    random_number = random.randint(1, 101)

    guess()
    
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        os.system('cls')
        guessing_game()
    else:
        exit()

guessing_game()
