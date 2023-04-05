# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:50:22 2023

@author: wooihaw
"""

from random import choice, shuffle

animals = ['wolf', 'whale', 'cheetah', 'lizard', 'tiger', 'monkey', 'parrot', 'gorilla', 'dolphin', 'snake']

while True:
    answer = choice(animals)
    guess = list(answer)
    shuffle(guess)
    
    response = input(f"Can you guess what is {''.join(guess)}? ")
    if response == answer:
        print("You are a genius!")
    else:
        print(f"You are wrong. The answer is {answer}")
    
    a = input("Do you want to continue (y/n)? ")
    if a.lower() == 'y':
        continue
    else:
        break