# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:58:05 2023

@author: wooihaw
"""

from collections import Counter

with open("data/alice.txt", "r") as f:
    s = f.read()  # read file into string
    t = [c.lower() if c.isalpha() else ' ' for c in s]  # clean and normalize text
    u = ''.join(t)  # convert back to string
    w = u.split()  # split into words
    count = Counter(w)  # count word frequency
    
    print(f"Number of unique words: {len(count)}")
    print(f"Top 10 more frequent words: {count.most_common(10)}")
    print(f"The word 'alice' appears {count['alice']} times.")