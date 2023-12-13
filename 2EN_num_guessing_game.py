#This program is a simple number guessing name. It generates a random number between 1 and 10 and prompts the user to guess the number. It provides feedback if the guessed numner
# is too small or too large and prompts the user to keep guessing until the correct number is successfully guessed!

import random

def game():
    computer_num = random.randint(1, 11)
    try:
        level = int(input("Level: "))
        while True:

                level = int(input("Guess: "))
                if level < computer_num:
                    print('Too small!')
                elif level > computer_num:
                    print('Too large!')
                else:
                    break
    except ValueError:
            level = int(input("Guess: "))

    return 'Just right!'

gamey = game()
print(gamey)


        
