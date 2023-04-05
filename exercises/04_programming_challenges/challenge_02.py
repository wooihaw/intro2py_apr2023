# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:46:03 2023

@author: wooihaw
"""

while True:
    try:
        principal = float(input("Enter the initial investment: "))
        interest = float(input("Enter the annual rate: "))
        years = int(input("Enter the years of investment: "))
    except:
        print("Invalid value!")
        continue
    else:
        print(f"Initial investment: ${principal:.2f}, annual rate: {interest}%, years of investment: {years}")
        for i in range(years):
            principal = principal + principal * interest/100
            print(f"Year {i+1}: $ {principal:.2f}")
        break