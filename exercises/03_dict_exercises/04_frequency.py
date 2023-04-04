# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'The quick brown fox jumps over the lazy dog.'

# Clean and normalize the text
alist = [c.lower() for c in astring if c.isalpha()]
print(alist)

freq = {c: alist.count(c) for c in sorted(set(alist))}
print(f"{freq = }")

# Use library function
from collections import Counter

count = Counter(alist)
print(count)