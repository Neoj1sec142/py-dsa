# dsa1.py
##### 1.1 #####
# Unpacking
p = (4,5)
x, y = p
# print(f'X: {x} | Y: {y}')

# data = ['ACME', 50, 91.1, (2012, 12, 21)]
# name, shares, price, date = data
# (yr, mon, day) = date
# print(f'It is the {day}st day of {mon}, {yr}')

s = 'Hello'
a,b,c,d,e = s
# print(f'{a}{b}{c}{d}{e}')

# To not use a specific value that you are
# unpacking use a throwaway variable like _
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
# print(f'{shares} going for {price}')

##### 1.2 #####

# Using an unknown number of variables use *
# record = ('Dave', 'dave@example.com', '773-555-8222', '847-555-1212')
# name, email, *phones = record
# for item in phones:
#     print(item)

# It can be extremely useful for tuples
records = [
    ('foo', 1,2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)

# Or when combined with string operations
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
# for field in fields:
    # print(f'User {uname} : {field} : {sh} is located at {homedir}')
   
data2 = ['ACME', 50, 91.1, (12, 21, 2012)]
name, *_, (*_, year) = data2
# print(f'{name} on the year {year}')

# Spliting the head and tail of a list
items = [1, 10, 7, 4, 5, 9]
# head, *tails = items
# for tail in tails:
#     print(f'Head: {head} | Tail: {tail}')
    
def sum(items):
    head, *tails = items
    return head + sum(tails) if tails else head

print(f'The sum of the items is: {sum(items)}')