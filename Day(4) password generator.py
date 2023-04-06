# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:40:07 2023

@author: DATA-JOHN
"""
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l',
         'm','n','o','p','q','r','s','t','u','v','w','x',
         'y','z','A','B','C','D','E','F','G','H','I','J',
         'K','L','M','N','O','P','Q','R','S','T','U','V',
         'W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

print("welcome to the password generator!")

number_of_letters=int(input("how many letters would you like in your password?\n"))
number_of_symbols=int(input("how many symbols would you like?\n"))
number_of_numbers=int(input("how many numbers would you like?\n"))

password_list=[]
for letter in range(1,number_of_letters+1):
    random_letter=random.choice(letters)
    password_list.append(random_letter)

for symbol in range(1,number_of_symbols+1):
    random_symbol=random.choice(symbols)
    password_list.append(random_symbol)
    
for number in range(1,number_of_numbers+1):
    random_number=random.choice(numbers)
    password_list.append(random_number)
    
#randomizing the password list
random.shuffle(password_list)
password=""

#changing a password from a list to a string
for char in password_list:
    password+=char

print(password)