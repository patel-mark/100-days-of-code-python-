# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:07:36 2023

@author: DATA-JOHN
"""


def prime_number(number):
    # Convert the input number to an integer
    number = int(number)

    if number > 1:
        # Check for factors
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
prime_number(9)