# Task_1
# v.1

from collections import Counter
text = 'A journey of a thousand miles begins with a single step.'
list_text = text.lower().replace('.', '').split()
counts = Counter(list_text)
print(counts)

# v.2

import string

s = 'A journey of a thousand miles begins with a single step.'

for x in string.punctuation:
    s = s.replace(x,'')

s = s.lower().split()

d = dict()
for x in s:
    if x in d:
        d[x] = d[x]+1
    else:
        d[x] = 1
print(str(d))


# Task_2

stock = {
    'banana':6, 
    'apple':0,
    'orange':32,
    'pear':15
    }
prices = {
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3
    }
# function which takes as input two dicts with structure mentioned above and
# computes and returns the total price of stock.

# v.1 by cycle for
s = 0
for fruit in stock.keys():
    s += stock[fruit]*prices[fruit]
print(s)

# v.2 by generate
s = sum(stock[fruit] * prices[fruit] for fruit in stock.keys())
print(s)


# Task_3

a = [value**2 for value in range(1, 11)]
print(a)


