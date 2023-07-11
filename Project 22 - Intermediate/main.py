import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row['letter']: row['code'] for _, row in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = list(input("Enter a word: ").upper())
coded_list = [nato_dict[x] for x in user_input]
print(coded_list)
