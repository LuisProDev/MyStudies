import random
import string

while True:
    letters = int(input("How many letters do you want? "))
    symbols = int(input("How many symbols do you want? "))
    numbers = int(input("How many numbers do you want? "))
    
    random_letters = []
    random_symbols = []
    random_numbers = []
    
    for i in range(0, letters):
        random_letters.append(random.choice(string.ascii_letters))
    for i in range(0, symbols):
        random_symbols.append(random.choice(string.punctuation))
    for i in range(0, numbers):
        random_numbers.append(random.choice(string.digits))
        
    all_lists = random_letters + random_numbers + random_symbols
    random.shuffle(all_lists)
    
    password = ''.join(all_lists)
    
    print(f"Here's your password: {password}")
    
    ending = input("Would you like to try again? Y/N: ").lower()
    if ending == 'y':
        continue
    else:
        break
