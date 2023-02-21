# dsa3.py - Implementing a Priority Queue
# Problem : trying to implement a queue that sorts
# items by a given priority and always returns the 
# item with the highest priority on each pop

import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Item:
    def __init__(self, name): 
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
    
# testing / usage
q = PriorityQueue()
q.push(Item('Buffalo Wild Wings'), 1)
q.push(Item('Culvers'), 5)
q.push(Item('Wendys'), 4)
q.push(Item('Taco Bell'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())