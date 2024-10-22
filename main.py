
stages = ['''
    +-----+
    |     |
    O     |
   /|\    |
   / \    |
          |
  ==========
''', '''
    +-----+
    |     |
    O     |
   /|\    |
   /      |
          |
  ==========
''', '''
    +-----+
    |     |
    O     |
   /|\    |
          |
          |
  ==========
''', '''
    +-----+
    |     |
    O     |
   /|     |
          |
          |
  ==========
''', '''
    +-----+
    |     |
    O     |
    |     |
          |
          |
  ==========
''', '''
    +-----+
    |     |
    O     |
          |
          |
          |
  ==========
''', '''
    +-----+
    |     |
          |
          |
          |
          |
  ==========
''', ]

import words
import random

random_word = random.choice(words.words_list)
random_word = list(random_word)

display_word = []
for n in random_word:
    display_word += "_"

print(''.join(display_word))
heart = "❤️"
life_counter = 6

while life_counter > 0 and "_" in display_word:
    guessed_letter = input("Guess a letter: \n").lower()

    for x in range(len(random_word)):
        if guessed_letter == random_word[x]:
            display_word[x] = guessed_letter
            if "_" not in display_word:
                print("You guessed the word right, YOU WIN! 🏆")

    for letter in guessed_letter:
        if guessed_letter not in random_word:
            life_counter -= 1
            print("Lives: " + life_counter * heart)
            if life_counter == 1:
                print("This is your last life! ❤️")
        
    print(''.join(display_word))
    print(stages[life_counter])
print("\n")

if life_counter == 0:
    print("Game Over!")
    print("The word was: ")
    print(''.join(random_word))
    print("\n")