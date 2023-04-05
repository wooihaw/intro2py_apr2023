# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:38:43 2023

@author: wooihaw
"""

# r - number of rabbits
# c - number of chickens
# c + r = 35
# 2*c+ 4*r = 94

for r in range(36):
    c = 35 - r
    if 2*c + 4*r == 94:
        print(f"There are {c} chickens and {r} rabbits.")