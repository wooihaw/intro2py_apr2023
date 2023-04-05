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




