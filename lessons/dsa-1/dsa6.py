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

rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter
from itertools import groupby
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('   ', i)

