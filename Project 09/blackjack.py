import random
import os
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Randomize cards
def card_dealer():
    return random.choice(cards)

#Calculate the score of cards, and check if there's a blackjack or if the user went over 21
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Compare the scores and check who won
def compare(computer_score, player_score):
    if player_score == computer_score:
        print("Draw")
    elif computer_score == 0:
        print("The computer won with a Blackjack!")
    elif player_score == 0:
        print("You've won with a Blackjack!")
    elif player_score > 21:
        print("You went over 21, you've lost!!")
    elif computer_score > 21:
        print("Computer went over!!")
    elif player_score > computer_score:
        print("You've won")
    else:
        print("You've lost")

def blackjack():
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0

    #Put the random cards in the player's and computer's deck
    for i in range(0,2):
        player_cards.append(card_dealer())
        computer_cards.append(card_dealer())

    #Check if the player won with a blackjack or lost with a deck over 21
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    while True:
        more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if more_cards == 'y':
            player_cards.append(card_dealer())
            player_score = calculate_score(player_cards)

            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer first card: {computer_cards[0]}")

            while computer_score < 17:
                computer_cards.append(card_dealer())
                computer_score = calculate_score(computer_cards)

        else:
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer first card: {computer_cards[0]}")

            
            while computer_score < 17:
                computer_cards.append(card_dealer())
                computer_score = calculate_score(computer_cards)

            time.sleep(2)
            print(f"Your final hand: {player_cards}, current score: {player_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            compare(computer_score, player_score)
           
            end_game = input("Do you want to play again? Type 'y' or 'n': ").lower()
            if end_game == 'y':
                os.system('cls')
                blackjack()
            else:
                os.system('cls')
                exit() 
        
blackjack()
        
            
