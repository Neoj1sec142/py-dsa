# dsa4.py - Mapping Keys to Multiple Values in a Dict
# ##### 1.6 ########
# import json
# from collections import defaultdict, OrderedDict
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)
# print(d)
# s = defaultdict(set)
# s['a'].add(1)
# s['a'].add(2)
# s['b'].add(4)
# print(s)
# Initializing first value
# Without default dict
# d = {}
# for key, value in pairs:
#     if key not in d: d[key] = []
#     d[key].append(value)
# Initializing first value
# Without default dict
# d = defaultdict(list) 
# for key, value in pairs: 
#     d[key].append(value)
# ##### 1.7 ########
# To preserve the order and the object
# use a OrderedDict
# useful for json
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['spam'] = 3
# d['grok'] = 4

# for key in d:
    # print(key, d[key])
    # EX json.dumps(d)

# ##### 1.8 ########
# Calculating with dictionaries
'''
It is useful to use the zip method 
to handle calculating keys with data
'''
stock_prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.50,
    'FB': 10.75
}
# min_price = min(zip(stock_prices.values(), stock_prices.keys()))
# print(f'Min: {min_price}')
# max_price = max(zip(stock_prices.values(), stock_prices.keys()))
# print(f'Max: {max_price}')
# '''
# Similarly you can use zip with sorted
# '''
# sorted_prices = sorted(zip(stock_prices.values(), stock_prices.keys()))
# count = 0
# for price in sorted_prices:
#     print(f'Item: {count} = {price}')
#     count += 1
'''
Sometimes you want to search a dictionaries
values and return the key of the selected item
EX below
'''
# print(f'Min: {min(stock_prices, key=lambda k: stock_prices[k])}')
# print(f'Max: {max(stock_prices, key=lambda k: stock_prices[k])}')
'''However to get the min value you have to provide a key'''
# min_val = stock_prices[min(stock_prices, key=lambda k: stock_prices[k])]
# print(f'Min Val: {stock_prices[min(stock_prices, key=lambda k: stock_prices[k])]}')
'''
It should be noted that if there are multiple
entries with the same value than the min
and max will return the lowwest value for
the keys to differentiate between entries
'''

# ##### 1.9 ########
