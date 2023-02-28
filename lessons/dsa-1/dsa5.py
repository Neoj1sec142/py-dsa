# ####### 1.10 #############
'''
If you want to eliminate the 
duplicate values in a sequence
but retain the order
'''

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            
# a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))
'''
Notice how this only works if the items
in the sequence are hashable, if you are
using an unhashable type such as dicts you
can modify as follows
'''

def flex_dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
'''This makes the dict iterable to filter through keys'''
a = [ { 'x': 1, 'y': 2}, { 'x': 1, 'y': 3}, { 'x': 1, 'y': 2}, { 'x': 2, 'y': 4}]
print(f"Dict Rem Dupes: {list(flex_dedupe(a, key=lambda d: (d['x'], d['y'])))}")

# ####### 1.11 #############
'''
Cleaning up a programs slices and indexs
can make a huge difference when making 
code more readable
'''