# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:12:22 2023

@author: wooihaw
"""

with open("data/Heathrow.txt", "r") as f:
    raw_data = f.readlines()
    temperatures = [float(i.strip()) for i in raw_data]
    temperatures.sort()
    n = len(temperatures)
    mean = sum(temperatures)/n
    
    if n%2 == 0:
        median = (temperatures[n//2-1] +temperatures[n//2]) / 2
    else:
        median = temperatures[n//2]
    
    print(f"Lowest: {temperatures[0]}, highest: {temperatures[-1]}")
    print(f"Mean: {mean:.2f}, median: {median}")