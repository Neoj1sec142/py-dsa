# ######## 2.14 ###########
'''
combining many small strings
together into a larger string.
enter the join() method
'''
# parts = ['Is', 'Chicago', 'Not', 'Chicago']
# print(' '.join(parts))
# print(','.join(parts))
# print(''.join(parts))
'''
One related (and pretty neat)
trick is the conversion of
data to strings and concatenation 
at the same time using a generator
expression
'''
# data = ['ACME', 50, 91.1]
# print(','.join(str(d) for d in data))
'''
Be aware of unnessecary string
concatenations
'''
# a = 'hour'
# b = 'min'
# c = 'sec'
# print(a + ':' + b + ':' + c) #Ugly
# print(':'.join([a,b,c])) # Still Ugly
# print(a, b, c, sep=':') #Better
'''
for i/O operatations if the strings you
want to join are large it may be better
to create a generator function
to emit fragments
'''
# def sample_gen():
#     yield 'Is'
#     yield 'Chicago'
#     yield 'Not'
#     yield 'Chicago?'
'''
you can then join the fragements #1,
redirect the fragements #2,
or you can come up with a hybrid scheme
thats smart about i/o operations #3
'''
#1
# text = ''.join(sample_gen())
# print(text)
#2
# for part in sample_gen():
    # f.write(part)
#3 
# def combine(source, maxsize):
#     parts = []
#     size = 0
#     for part in source:
#         parts.append(part)
#         size += len(part)
#         if size > maxsize:
#             yield ''.join(parts)
#             parts = []
#             size = 0
#     yield ''.join(parts)
# for part in combine(sample_gen(), 32768):
#     # print(part)
#     pass
'''
The key point is that the 
original generator function doesn't 
have to know the precise
details. It just yields the parts.
'''
# ######## 2.15 ###########
'''
You want to create a string in 
which embedded variable names 
are substituted with a string 
representation of a variable's value.
'''
s = '{name} has {n} messages.'
# print(s.format(name='Guildo', n=37))
# If the variables are truely variables you can
# Use the vars() function
# name = 'Guildo'
# n = 37
# print(s.format_map(vars()))

# You can also use vars() with an instance
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
class safesub(dict):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    def __missing__(self, key):
        return '{' + key + '}'

# a = safesub('Guildo')
# print(s.format_map(safesub(vars())))
# Now you  can :
import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
# name = 'Neo'
# n = 31
# print(sub('Hello {name}'))
# print(sub('You have {n} messages'))
# ######## 2.16 ###########
''''''
# ######## 2.17 ###########
''''''