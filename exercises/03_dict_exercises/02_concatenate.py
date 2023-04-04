# Write a Python script to concatenate following dictionaries to create a new one.
# Expected Result: 
# d4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40}
d3 = {'e': 50}

# Use union operator
d4 = d1 | d2 | d3
print(f"{d4 = }")

# Use the dicionary unpacking
d4_2 = {**d1, **d2, **d3}
print(f"{d4_2 = }")

# Use update() method
d4_3 = {}
for d in (d1, d2, d3):
    d4_3.update(d)
print(f"{d4_3 = }")