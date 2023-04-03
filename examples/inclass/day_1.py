# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:20:18 2023

@author: wooihaw
"""

#%% Numeric data types
a = 1234567890
b = a ** 100
print(a, b)
print(a.__sizeof__())
print(b.__sizeof__())

#%% Binary and hexadecimal numbers
a = 0b10110010
b = 0x123def
c = a + b

print(a, b, c)
print(bin(a))
print(hex(b))
print(bin(c), hex(c))

#%% Variables
# continue = 1  # Using keyword as variable name will cause a syntax error
# type = 1  # However, you can shadow a built-in function

this_is_a_long_variable_name = 123.45
# 1star = 23456  # Variable name cannot start with digit
_1star = 23456  # We can start with underscore

#%% Converting between data types
a, b, c = 1, 2.5, 'adc'

d = float(a)
e = int(b)
# f = int(c) #  Cannot convert alphabets to integer

f = int(c, base=16)

print(d, e, f, sep=',')

g = str(b)
# h = g + 3  # cannot add a string to a number

#%% Operators
ans1 = -2 ** 2
print(ans1)

ans2 = (-2) ** 2
print(ans2)

#%% Comparison operators
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 20)
print(0 <= b < 20)

#%% Strings
s1 = "It's a python."
s2 = 'It\'s a python.'
print(s1, s2, sep='\n')

s3 = 'John said "Yes, I am alone."'
print(s3)

s4 = '''This is a multiline string that is very long
and spans multiple lines.'''

s5 = """This is another multiline string that is very long
and spans multiple lines."""
print(s4, s5, sep='\n')

#%% String indexing and slicing
s = "Introduction to Python"
print("Fist character: ", s[0])
print("last character: ", s[-1])

t = s[:12]  # first 12 characters
u = s[-6:]  # last 6 characters
print(t, u, sep=",")

print(s[::-1])  # reverse order of the characters

v = t + u
print(v)

print(3 * t)
print(5 * u)

#%% String methods
s = "Python is awesome!"

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.replace('o', 'u'))
print(s)  # the string s does not change

t = 'abc123'
print(t.isalnum())
print(t.isalpha())
print(t.isdigit())

u = '   This is a test.  \n'
print(u)
print(u.strip())
print(u.lstrip())
print(u.rstrip())

print("The character 'o' appears", s.count('o'), "times.")

#%% f-string formating
a = 123
b = 45.678
print(f"{a = }, {a = :04x}, {a = :08b}")
print(f"{b = :.0f}, {b = :.1f}, {b = :.2f}")

print("Python is a \N{snake}")

#%% List join, append and extend
alist = [1, 2, 3]
print(f"{alist = }")

alist = alist + [4]  # can only join with another list
print(f"{alist = }")

alist += [5]  # same as above (alist = alist + [5])
print(f"{alist = }")

alist.append(6)  # Only can append one item at a time
print(f"{alist = }")

alist.extend([7, 8])  # similar to alist = alist + [7, 8]
print(f"{alist = }")

print(f"{len(alist)=}")  # use len() function to check the number of items

#%% Sorting a list
blist = [3, 1, 4, 2, 6, 5, 0]
clist = sorted(blist)
dlist = sorted(blist, reverse=True)
print(f"{blist=}, {clist=}, {dlist=}")

elist = blist.sort()
print(f"{blist=}, {elist=}")

#%% String to list and vice-versa
astring = 'Testing 123'
alist = list(astring)
print(f"{astring = }")
print(f"{alist = }")

alist[1] = 'a'
print(f"{alist = }")

bstring = ''.join(alist)
print(f"{bstring = }")

cstring = '--'.join(alist)
print(f"{cstring = }")

#%% List methods
alist = [1, 2.3, 'abc', [3, 7.8], 'xyz', 101, 1]

print(f"{alist.count(1)=}")

print(f"{alist.index('abc')=}")

print(f"{alist.index(1)=}")  # only return the first occurance

alist.remove(1)
print(f"{alist=}")  # only remove the first occurance

alist.insert(2, "Hello")
print(f"{alist=}")

a = alist.pop(4)
print(f"{a=}")
print(f"{alist=}")

alist.clear()
print(f"{alist=}")

blist = [1, 2.3, 'abc', [3, 7.8], 'xyz', 101, 1]
print(f"{blist[3][1]=}")

#%% Dictionary methods
adict = dict(a=1, b=2.5, c='abc')
# print(f"{adict['d']=}")  # KeyError as the key 'd' cannot be found
print(f"{adict.get('d', None)=}")

print(f"{adict.setdefault('d', 4)}")
print(f"{adict = }")

#%% Joining 2 dictionaries
d1 = dict(a=1, b=2, x=0)
d2 = dict(x=3, y=4, z=5)

# Method 1
d3 = d1.copy()
d3.update(d2)
print(f"{d3 = }")

# Method 2
d4  = {**d1, **d2}
print(f"{d4 = }")

# Method 3 - Using the union operator
d5 = d1 | d2
print(f"{d5 = }")

#%% Set operations
alist = [1, 2, 1, 3, 4, 1, 5, 2, 0, 2.5, 'abc']
aset = set(alist)
blist = list(aset)
print(f"{aset = }")
print(f"{blist = }")
