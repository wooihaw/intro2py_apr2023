# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 09:37:25 2023

@author: wooihaw
"""

#%% Exception Handling

while True:
    try:
        num = int(input("Enter an integer: "))
    except Exception as e:
        print(type(e))
        print(f"Error: {e}")
        continue
    else:
        print(f"You have entered {num}")
        break

#%% Functions are objects
def func1(x):
    return x + 1

def func2(x):
    return x + 2

def func3(x):
    return x + 3

functions = (func1, func2, func3)

for f in functions:
    print(f(10))
    
d_functions = {'function1': func1, 'function2': func2, 'function3': func3}
for k in d_functions:
    print(f"{k}: {d_functions[k](20)}")

#%% Lambda function
a = [ (1,2), (11,-3), (5,10), (3,1) ]
print(sorted(a))

# Use normal function
def f1(x):
    return x[1]
print(sorted(a, key=f1))

# Use lambda function
print(sorted(a, key=lambda x: x[1]))

#%% Lambda function example 2

IDs = ['ID21', 'ID7', 'ID57', 'ID101', 'ID3', 'ID86', 'ID33']
print(sorted(IDs))
print(sorted(IDs, key=lambda x:int(x[2:])))

#%% Lambda function example 3

papers = ('A1', 'A4', 'A3', 'A2', 'A5')

print(f"Biggest paper: {max(papers)}")

print(f"Biggest paper: {max(papers, key=lambda x: -int(x[1]))}")

#%% map() function

words = ['apple', 'bell', 'cat', 'dog', 'egg', 'fish']

# Use for loop
r1 = []
for w in words:
    r1.append(w[::-1])
print(f"{r1 = }")

# Use list comprehension
r2 = [w[::-1] for w in words]
print(f"{r2 = }")

# Use map() function
r3 = list(map(lambda w: w[::-1], words))
print(f"{r3 = }")

#%% filter function
# Select only the words with 3 characters
words = ['apple', 'bell', 'cat', 'dog', 'egg', 'fish']

# Use for loop
t1 = []
for w in words:
    if len(w) ==  3:
        t1.append(w)
print(f"{t1 = }")

# Use list comprehension
t2 = [w for w in words if len(w) == 3]
print(f"{t2 = }")

# Use filter() function
t3 = list(filter(lambda w: len(w) == 3, words))
print(f"{t3 = }")

#%% Object oriented programming

class Square:
    def __init__(self, length):
        self.length = length
    def __str__(self):
        return f"This is a square with length of {self.length}"
    def area(self):
        return self.length * self.length
    def perimeter(self):
        return self.length * 4
    def __eq__(self, other):
        return self.length == other.length
    def __add__(self, other):
        return self.area() + other.area()
    def __repr__(self):
        return f"Square with length {self.length}"

sqr1 = Square(5)
print(sqr1)
print(f"Area: {sqr1.area()}")
print(f"Perimeter: {sqr1.perimeter()}")

sqr2 = Square(6)
print("Same size" if sqr1 == sqr2 else "Not the same size")

print(sqr1 + sqr2)


