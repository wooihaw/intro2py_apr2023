# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:55:50 2023

@author: wooihaw
"""

s1 = set(range(5, 101, 5))  # set of numbers which are divisible by 5
s2 = set(range(7, 101, 7))  # set of numbers which are divisible by 7
s3 = set(range(1, 101))  # set of numbers from 1 to 100

print(f"Numbers from 1 to 100 which are not divisible by 5 or 7: {s3 - (s1 | s2)}")

# Use list comprehension
s4 = [i for i in range(1, 101) if i%5 and i%7]
print(f"Numbers from 1 to 100 which are not divisible by 5 or 7: {s4}")