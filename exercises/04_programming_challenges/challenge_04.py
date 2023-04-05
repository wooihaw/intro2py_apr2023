# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:04:09 2023

@author: wooihaw
"""

data = {}
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    age = input(f"Enter age {i+1}: ")
    data[name] = age

name = input("Enter a name to search for age: ")
print(f"{name} is {data.get(name, 'unknown')} years old.")