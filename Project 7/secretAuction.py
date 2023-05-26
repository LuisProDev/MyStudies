import os

print("Welcome to the secret auction program.")

bids = {}

def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $")) 
    bids[name] = bid   
    new_players = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if new_players == 'yes':
        os.system("cls")
        continue
    else:
        highest_bidder(bids)
        break
        
