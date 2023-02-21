# dsa2.py

###### 1.3 ######
# from collections import deque

def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)

##### 1.4 #####
# making lists of the smallest or largest numbers
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]  
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))
# both functions accept a key param to allow
# them to be used with more complicated stuctures
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
       {'name': 'FB', 'shares': 200, 'price': 21.09},
       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
       {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(f'Cheap: {cheap}')
print(f'Expensive: {expensive}')