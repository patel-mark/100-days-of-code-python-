# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:31:03 2023

@author: DATA-JOHN
"""

# Define the alphabet list that will be used for encryption and decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Prompt the user to input the direction of the operation, the message to be encrypted/decrypted, and the number of positions to shift each letter
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

# If the direction is 'encode', define an encrypt function that takes the message and shift number as arguments
if direction == "encode":
    def encrypt(text, shift):
        cipher_text = ""  # Initialize an empty string to store the encrypted message
        for letter in text:  # Iterate through each letter of the message
            position = alphabet.index(letter)  # Find the index of the letter in the alphabet list
            new_position = position + shift  # Add the shift number to the index to get the new index of the shifted letter
            new_letter = alphabet[new_position]  # Find the letter at the new index in the alphabet list
            cipher_text += new_letter  # Append the new letter to the cipher_text string
        print(f"Our encrypted message is {cipher_text}")  # Print the encrypted message

    encrypt(text, shift)  # Call the encrypt function with the user input values

# If the direction is 'decode', define a cipher function that takes the message and shift number as arguments
elif direction == "decode":
    def cipher(text, shift):
        cipher_text = ""  # Initialize an empty string to store the decrypted message
        for letter in text:  # Iterate through each letter of the message
            position = alphabet.index(letter)  # Find the index of the letter in the alphabet list
            new_position = position - shift  # Subtract the shift number from the index to get the new index of the shifted letter
            new_letter = alphabet[new_position]  # Find the letter at the new index in the alphabet list
            cipher_text += new_letter  # Append the new letter to the cipher_text string
        print(f"{cipher_text} is our decrypted text")  # Print the decrypted message

    cipher(text, shift)  # Call the cipher function with the user input values

# If the direction is neither 'encode' nor 'decode', print an error message
else:
    print("Error in direction")
