import pandas as pd

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in phonetic_data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the word: ")
phonetic_list = [phonetic_dict[f"{letter.upper()}"] for letter in word]
print(phonetic_list)