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













