# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:43:37 2023

@author: DATA-JOHN
"""

word_list=["ardvark","baboon","camel"]

import random
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
end_of_game=False
lives=6

for letter in range(len(chosen_word)):
     display+="_"
print(display)
 
while end_of_game==False:
   guess=input("choose a letter: ").lower()

   for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
   print(display)
   
   if guess not in chosen_word:
       lives-=1
       if lives==0:
           end_of_game=True
           print("out of lives")
    
   if "_" not in display:
        end_of_game=True
        print("you win")
        