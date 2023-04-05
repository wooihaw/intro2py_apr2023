# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:27:03 2023

@author: wooihaw
"""

def convert_cel_to_far(c: float) -> float:
    return c * 9/5 + 32

def convert_far_to_cel(f: float) -> float:
    return  (f - 32) * 5/9

f = float(input("Enter temperature in degrees Fahrenheit: "))
print(f"It is equivalent to {convert_far_to_cel(f):.2f}{0x00b0:c}C")

c = float(input("Enter temperature in degrees Celsius: "))
print(f"It is equivalent to {convert_cel_to_far(c):.2f}{0x00b0:c}F")