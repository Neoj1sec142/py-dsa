# ######## 1.13 ###########
'''
sorting a list of dictionaries
by one or more values. 
Using the itemgetter is actually
a but faster than using a lambda
if performance is a concern
'''
# from operator import itemgetter
# rows = [
#         {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#         {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#         {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#         {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# print(rows_by_fname)
# print(rows_by_uid)

# ######## 1.14 ###########
'''
If you want to sort objects of the same
class but they dont support comparison
operations, similiarly faster than lambda
'''
# from operator import attrgetter
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
    
users = [User(23), User(3), User(99)]
# print(sorted(users, key=lambda u: u.user_id))
# print(sorted(users, key=attrgetter('user_id')))

# ######## 1.15 ###########
'''
if you have a sequence f dictionaries
or instances and you want to iterate 
over a field, itertools.groupby()
'''

# rows = [
#         {'address': '5412 N CLARK', 'date': '07/01/2012'},
#         {'address': '5148 N CLARK', 'date': '07/04/2012'},
#         {'address': '5800 E 58TH', 'date': '07/02/2012'},
#         {'address': '2122 N CLARK', 'date': '07/03/2012'},
#         {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#         {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#         {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#         {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]
# from operator import itemgetter
# from itertools import groupby
# rows.sort(key=itemgetter('date'))
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print('   ', i)

# ######## 1.16 ###########
'''
You have data inside of a sequence, and 
need to extract values or reduce the sequece
using some criteria - the easiest is using list 
comprehension
'''
# mylist = [1,4,-5,10,-7,2,3,-1]
# print([n for n in mylist if n > 0])
# print([n for n in mylist if n < 0])
'''
The downside to list comprehension, is
that if the original input is large, the
list comp will produce a large result. If
this is a concern you can use generators 
produce filtered values
'''
# pos = (n for n in mylist if n > 0)
# print(pos)
# for x in pos:
#     print(x)
'''
Sometimes when you have complex processes
such as exception handling etc you can 
put the filtering code into its own function
'''
# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
# We need the list() because filter
# creates an iterator
# ivals = list(filter(is_int, values))
# Here we are turning an array into
# a filtered list that uses the is_int
# function to filter the values
# print(f'Filtered Values: {ivals}')

# You can also change data with list comp
# mylist = [1,4,-5,10,-7,2,3,-1]
# import math
# print([math.sqrt(n) for n in mylist if n > 0])

# or maybe adding a default for negative or null fields
# clipped = [n if n > 0 else 0 for n in mylist]
# print(clipped)

'''
Another notable filtering tool 
is itertools.compress()
'''
# addresses = [
#         '5412 N CLARK',
#         '5148 N CLARK',
#         '5800 E 58TH',
#         '2122 N CLARK'
#         '5645 N RAVENSWOOD',
#         '1060 W ADDISON',
#         '4801 N BROADWAY',
#         '1039 W GRANVILLE',
#     ]
# counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
# Now suppose u want to make a list
# where the corresponding value > 5
# from itertools import compress
# more5 = [n > 5 for n in counts]
# print(list(compress(addresses, more5)))