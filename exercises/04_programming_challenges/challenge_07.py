# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:36:57 2023

@author: wooihaw
"""

# Using map() and filter()
sqr1 = list(map(lambda y: y*y, filter(lambda x: x%2==0, range(1, 101))))
print(f"{sqr1 = }")

# Using list comprehension
sqr2 = [i*i for i in range(1, 101) if i%2==0]
print(f"{sqr2 = }")