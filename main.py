# Todo: Add a counter for letters used

import random
import os
from words_list import *
from stages_lives import *

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

while True:
    clear()
    
    end_of_game = False
    lives = 6
    
    difficulty_choice = False
    while difficulty_choice == False:
        logo()
    
        difficulty = input("""\33[1m---Choose your difficulty---\33[0m
\33[32mEasy (For you)\33[0m / \33[34mNormal (A bit hard for you)\33[0m / \33[31mHard (Don't even bother)\33[0m
""").lower()
    
        clear()
        
        if difficulty == "hard":
            difficulty_choice = True
            chosen_word = random.choice(hard_words)
            # word_def = hard_word_dict[chosen_word]
            # print(f'Pssst, the solution is {chosen_word}.')
        
        elif difficulty == "normal":
            difficulty_choice = True
            chosen_word = random.choice(normal_words)
            # print(f'Pssst, the solution is {chosen_word}.')
            
        elif difficulty == "easy":
            difficulty_choice = True
            chosen_word = random.choice(easy_words)
            # print(f'Pssst, the solution is {chosen_word}.')
        
        else:
            print("\n\33[31m[Invalid difficulty]\33[0m\n")
    
    display = []
    for letter in range(len(chosen_word)):
        display += "_"    
    
    # if difficulty == "hard":
    #     print("Type \33[33m[hint]\33[0m for hint.\n")
    
    logo()
    print(f"\n\33[34m{' '.join(display).upper()}\33[0m")
    
    while not end_of_game:
        guess = input("\nGo on. Try to guess a letter.\n").lower()
        
        #Use the clear() function imported from replit to clear the output between guesses.
        clear()
    
        logo()
        # if guess == "hint":
        #     print("\33[33mHint:\33[0m\n" + hard_word_dict[chosen_word])
    
        if guess in display:
            print(f"Cannot see? \33[34m{guess.upper()}\33[0m was already guessed.")
        
        else:
            
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = guess
                    print(f"Number of lives = \33[1;31m{lives}\33[0m")    
    
    
            if guess not in list(chosen_word):
                lives -= 1
                print("Lol. Wrong. As expected. Your short life -1.")
                print(f"Number of lives = \33[1;31m{lives}\33[0m")    
                if lives == 0:
                    end_of_game = True
                    print("\n\33[1;31mTsk tsk. This too hard for you? Hit [Enter] and choose easy.\33[0m")
                    print("\nThe word is " + "\33[34m" + chosen_word.upper() + "\33[0m")
                    # if difficulty == "hard":
                    #     print("\nThe word is " + "\33[34m" + chosen_word.upper() + "\33[0m" + ":\n" + hard_word_dict[chosen_word])
                    # else:
                    #     print("\nThe word is " + "\33[34m" + chosen_word.upper() + "\33[0m")
        
            if "_" not in display:
                end_of_game = True
                print("\n\33[1;32mThe game spoonfed you. Want to prove me wrong? Hit [Enter] then.\33[0m")
                print("\nThe word is " + "\33[34m" + chosen_word.upper() + "\33[0m")
                # if difficulty == "hard":
                #     print("\33[34m" + chosen_word.upper() + "\33[0m" + ":\n" + hard_word_dict[chosen_word])
                # else:
                #     print("\nThe word is " + "\33[34m" + chosen_word.upper() + "\33[0m") 
            
        print(stages[lives])
    
        print(f"\33[34m{' '.join(display).upper()}\33[0m")

    input()