import random
from art import *
from word_list import *

while True:

    print(logo)
    print("Welcome to my Hangman game!!")

    display = []
    random_word = random.choice(word_list)
    lives = 6

    for i in range(0, len(random_word)):
        display.append("_")
        
    while "_" in display:
        guess = input("Guess a letter: ").lower()
        for i, item in enumerate(random_word):
            if item == guess:
                display[i] = item
                
        if guess not in random_word:
            lives -= 1
            print(stages[lives])
            if lives == 0:
                print("You lost!")
                exit()
            
        print(display)
        if not "_" in display:
            print("You win!")
            print(victory)

    ending = input("Do you want to play again? Y/N: ").lower()
    if ending == 'y':
      continue
    else:
      break
    