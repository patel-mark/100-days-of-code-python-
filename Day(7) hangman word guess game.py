# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:43:37 2023

@author: DATA-JOHN
"""



import random

# A list of words to choose from
word_list=["ardvark","baboon","camel"]

# Picks a random word from the list
chosen_word = random.choice(word_list)

# For debugging purposes, prints the chosen word
print(chosen_word)

# Initializes the display list with underscores for each letter in the chosen word
display = []
for letter in range(len(chosen_word)):
     display += "_"

# For debugging purposes, prints the initial display list
print(display)

# Initializes the game loop
end_of_game = False

# Initializes the number of lives the player has
lives = 6

# The main game loop
while not end_of_game:
    
    # Prompts the user to input a letter
    guess = input("Choose a letter: ").lower()

    # Loops through each letter in the chosen word to see if it matches the user's guess
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            # If the letter matches the user's guess, replace the underscore in the display with the letter
            display[position] = letter
    
    # Prints the updated display list after the user's guess
    print(display)

    # If the user's guess is not in the chosen word, decrement the number of lives
    if guess not in chosen_word:
        lives -= 1
        
        # If the user has no more lives, the game ends
        if lives == 0:
            end_of_game = True
            print("Out of lives. Game over.")
    
    # If there are no more underscores in the display list, the player wins
    if "_" not in display:
        end_of_game = True
        print("You win!")
