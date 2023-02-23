# dsa4.py - Mapping Keys to Multiple Values in a Dict
import json
from collections import defaultdict, OrderedDict
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
# To preserve the order and the object
# use a OrderedDict
# useful for json
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])
    # EX json.dumps(d)