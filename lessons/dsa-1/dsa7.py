# ######## 1.17 ###########
'''
you want to make a dictionary that is a 
subset of another dictionary - dict comprehension
'''
# prices = {
#        'ACME': 45.23,
#        'AAPL': 612.78,
#        'IBM': 205.55,
#        'HPQ': 37.20,
#        'FB': 10.75
# }
# Make a dict of all prices over 200
# p1 = { key:val for key, val in prices.items() if val > 200}
# print(f'P1:{p1}')
# make a dict of tech stocks
# tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
# p2 = { key:val for key, val in prices.items() if key in tech_names }
# print(p2)
'''
much of what can be done with compehensions can also
be done by creating a sequence of tuples and passing 
them to the dict() function - however comprehension is 
much faster in account of efficiency
'''
# p3 = dict((key, val) for key, val in prices.items() if val > 200)
# print(f'P3: {p3}')

# ######## 1.18 ###########
'''
identifying elements based on name
rather than position, mapping names
to a sequence - collections.namedtuple()
'''
# from collections import namedtuple
# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# sub = Subscriber('jonesy@example.com', '2012-10-19')
# print(sub.addr)

'''
References to positional elements often 
make the code a bit less expressive and more
dependent on the structure of the records.
'''
# from collections import namedtuple
# Stock = namedtuple('Stock', ['name', 'shares', 'price'])
# google = Stock('Google', '5.76M', '1.3k')
# # print(google.shares)
# def compute_cost(records): 
#     total = 0.0
#     for rec in records: 
#         s = Stock(*rec)
#         total += s.shares * s.price 
#     return total

# replacing the values of a nametuple
# s = google._replace(shares='5.9M')
# print(s)

# usign a prototype with defaults and replacing 
#  with data instead of ending up with nulls
# Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# stock_proto = Stock('', 0, 0.0, None, None)
# def dict_to_stock(s):
#     return stock_proto._replace(**s)
# a = { 'name': 'ACME', 'shares':100, 'price': 123.45 }
# print(dict_to_stock(a))
# b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
# print(dict_to_stock(b))
# ######## 1.19 ###########
'''
an elegant way to combine data transformation
and reduction is to use a generator expression
'''
# nums = [1, 2, 3, 4, 5]
# s = sum(x * x for x in nums)
# print(s)
'''
to determine if any .py files live in
a directory
'''
# import os
# file = os.listdir('dirname')
# if any(name.endswith('.py') for name in file):
#     print('There be python')
# else:
#     print('Sorry no python')
'''
output a tuple as csv
'''
# s = ('ACME', 50, 123.45)
# print(','.join(str(x) for x in s))
'''
data reduction across fields of a data structure
'''

# portfolio = [
#     {'name':'GOOG', 'shares': 50},
#     {'name':'YHOO', 'shares': 75},
#     {'name':'AOL', 'shares': 20},
#     {'name':'SCOX', 'shares': 65}
# ]
# min_shares = min(s['shares'] for s in portfolio)
# print(min_shares)

# ######## 1.20 ###########

'''
You have multiple dictionaries or mappings that 
you want to logically combine into a single mapping 
to perform certain operations, such as looking up 
values or checking for the existence of keys.
'''

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
# say you need to search a first then b
# from collections import ChainMap
# c = ChainMap(a,b)
# print(c['x'])
# print(c['y'])
# print(c['z'])
# values = ChainMap()
# values['x'] = 1
# values = values.new_child()
# values['x'] = 2
# values = values.new_child()
# values['x'] = 3
# print(values.parents)