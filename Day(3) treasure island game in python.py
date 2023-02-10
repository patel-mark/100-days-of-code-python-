# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 23:49:09 2023

@author: DATA-JOHN
"""

option_one=input("left or right?:")
option_one=option_one.lower()
if option_one=="left":
  option_two=input("swim or wait?")
  option_two=option_two.lower()
  if option_two=="wait":
    option_three=input("which door?")
    option_three=option_three.lower()
    if option_three=="red":
      print("burned by fire.\n" "Game over")
    elif option_three=="blue":
      print("eaten by beasts.\n" "Game over.")
    elif option_three=="yellow":
      print("you win")
    else:
      print("Game over")
  else:
    print("attacked by trout.\n"
    "Game Over")
else:
  print("fall into a hole.\n" "Game over.")

