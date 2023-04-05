# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:41:44 2023

@author: wooihaw
"""

class Circle:
    __pi = 3.142
    a = 123
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.__class__.__pi * self.radius ** 2
    def circumference(self):
        return 2 * self.__class__.__pi * self.radius

c1 = Circle(4)
print(f"Area: {c1.area()}, circumference: {c1.circumference()}")
