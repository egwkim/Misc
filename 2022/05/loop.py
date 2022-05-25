"""
Modified collatz conjecture

f(x) = n/2     if n is even
       7n + 1  otherwise

The trivial cycle is 1 -> 8 -> 4 -> 2-> 1 (length 4)
"""

import os

l = []
x = 3
i = 0

path = os.path.join(os.path.dirname(__file__), 'numbers.txt')
print(path)

if os.path.exists(path):
    with open(path, 'r') as f:
        for line in f.readlines():
            l.append(int(line.split()[1]))
        i = len(l)
        x = l[-1]
        if x % 2:
            x = x*7+1
        else:
            x //= 2

with open(path, 'a') as f:
    while not x in l:
        i += 1
        l.append(x)
        print(i, x)
        f.write(f'{i} {x}\n')
        if x % 2:
            x = x*7+1
        else:
            x //= 2
    print('loop found!')
    start = x
    start_index = l.index(x) + 1
    end = l[-1]
    end_index = i
    print(f'from index {start_index} to {end_index}')
    print(f'length {end_index - start_index}')
    print(f'start value = {start}')
    print(f'end value = {end}')
