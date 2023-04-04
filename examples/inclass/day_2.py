# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:52:26 2023

@author: wooihaw
"""

#%% Conditional statement

a = 49
if a >= 50:
    print("Pass 1")
    print("Pass 2")
    print("Pass 3")
else:
    print("Fail 1")
    print("Fail 2")
print("Outside if-else statements")

#%% Ternary operator

marks = 85

if marks >= 50:
    print("You have passed")
else:
    print("You have failed")
    
print(f"You have {'passed' if marks >= 50 else 'failed'}")

#%% False value testing

alist = []

if len(alist) > 0:
    print("Not empty list")
else:
    print("Empty list")

if alist:
    print("Not empty list")
else:
    print("Empty list")

#%% for loop example 1
# Get a list of unique items
alist = [1, 2, 1, 5, 'a', 'b', 'a', 2, 'c']

# Using for loop
ulist1 = []
for i in alist:
    if i not in ulist1:
        ulist1.append(i)
print(f"{ulist1 = }")

# Using set
print(f"{list(set(alist)) = }")

#%% for loop example 2
# Using zip() to iterate multiple lists

fruits = ['apple', 'orange', 'durian', 'mango']
prices = [1.5, 2.5, 15]

for i, j in zip(fruits, prices):
    print(f"{i}: RM{j:.2f}")
    
# Use enumerate to automatically index the iteration
for i, (j, k) in enumerate(zip(fruits, prices), start=1):
    print(f"{i}. {j.capitalize():<8}: RM{k:>6.2f}")
    
#%% Using pass keyword and ellipsis

for i in range(10):
    pass
    
for j in range(10):
    ...

for _ in range(5):
    print("Test")

k = 50
if k > 100:
    ...

#%% Using break and continue keywords

while True:
    name = input("Enter you name: ") or "Noname"
    print(f"Hello {name}")
    ans = input("Do you want to continue? ")
    if ans.lower() in ('y', 'yes'):
        continue
    break

#%% List comprehension example 1
names = ['ali', 'bala', 'chen', 'dave']

# Use for loop
cap_names1 = []
for n in names:
    cap_names1.append(n.capitalize())
print(f"{cap_names1 = }")

# Use list comprehension
cap_names2 = [n.capitalize() for n in names] 
print(f"{cap_names2 = }")

#%% List comprehension example 2
languages = ['Java', 'Rust', 'C++', 'Swift', 'Go', 'Julia', 'Python']

# Use for loop
filtered_list1 = []
for i in languages:
    if 'o' in i:
        filtered_list1.append(i)
print(f"{filtered_list1 = }")

# Use list comprehension
filtered_list2 = [i for i in languages if 'o' in i]
print(f"{filtered_list2 = }")

#%% List comprehension example 3
# Calculate the number of odd numbers in a list
from random import randint

numbers = [randint(1, 100) for _ in range(100)]

print(f"There are {sum([1 if i%2 else 0 for i in numbers])} odd numbers")









