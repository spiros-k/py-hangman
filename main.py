words_list = ["vocabulary", "reflection", "impression", "establishment", "lifestyle", 
             "anticipation", "retirement", "initiative", "coincidence", "contradiction", 
             "extraterrestrial", "performance", "chocolate", "partnership", "consideration", 
             "entitlement", "imaginary", "irritating", "secretive", "competitive", 
             "increadible", "invincible", "invisible", "imaginary", "formulate", "pronounce", 
             "strengthen", "encounter", "reproduce", "concentrate", "challenge", "respectable", 
             "wilderness", "articulate", "operation", "notorious", "headquarters", 
             "premature", "announcement", "reasonable", "overwhelmed", "treasurer", 
             "translate", "countryside", "reproduction"]

import random

random_word = random.choice(words_list)
print(random_word)
display_word = ""
word_length = len(random_word)

user_guess = input("Guess a letter: \n").lower()
for letter in random_word:
    if letter == user_guess:
        display_word += letter
    else:
        display_word += "_"

print(display_word) 