import time
import random
import os
from database import *
from art import *

def higher_lower():
    choice_1 = random.choice(data)
    choice_2 = random.choice(data)
    score = 0 
    
    print(logo)
    time.sleep(1)
    print(f"Compare A: {choice_1['name']}, a/an {choice_1['description']}, from {choice_1['country']}")
    print(vs)
    time.sleep(1)
    print(f"Against B: {choice_2['name']}, a/an {choice_2['description']}, from {choice_2['country']}")
    winner = input("Who has more followers? 'A' or 'B': ").lower()
    
    if (choice_1['follower_count'] > choice_2['follower_count'] and winner == 'a') or (choice_2['follower_count'] > choice_1['follower_count'] and winner == 'b'):
        while True:
            choice_1 = choice_2
            choice_2 = random.choice(data)
            
            if choice_2 == choice_1:
                choice_2 = random.choice(data)
            
            os.system('cls')
            score += 1
            print(logo)
            time.sleep(1)
            print(f"You're right. Current Score: {score}")
            print(f"Compare A: {choice_1['name']}, a/an {choice_1['description']}, from {choice_1['country']}")
            print(vs)
            time.sleep(1)
            print(f"Against B: {choice_2['name']}, a/an {choice_2['description']}, from {choice_2['country']}")
            winner = input("Who has more followers? 'A' or 'B': ").lower()
                    
            if (choice_1['follower_count'] > choice_2['follower_count'] and winner == 'a') or (choice_2['follower_count'] > choice_1['follower_count'] and winner == 'b'):
                os.system('cls')
                continue
            else:
                os.system('cls')
                print(f"Sorry, that's wrong. Final Score: {score}")
                exit()
    else:
        os.system('cls')
        print(f"Sorry, that's wrong. Final Score: {score}")
        exit()

    
higher_lower()