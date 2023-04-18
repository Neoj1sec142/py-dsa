# ######## 2.1 ###########
'''
when trying to split a str in python
the split() does not allow for more than
one delimiter or handle white space before
or after delimiters - re.split() (more flexible)
'''
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
# print(re.split(r'[:,\s]\s*', line))
# be careful of capture groups though (they capture the delimiters)
fields = re.split(r'(;|,|\s)\s*', line)
# print(fields)
# # it can be useful in certain contexts though
# values = fields[::2]
# delimiters = fields[1::2] + ['']
# print(values, "VALS")
# print(delimiters, "DELIM")
'''
If you don't want the separator characters in
the result, but still need to use parentheses 
to group parts of the regular expression pattern, 
make sure you use a noncapture group, 
specified as (?:...)
'''
# print(re.split(r'(?:,|;|\s)\s*', line))

# ######## 2.2 ###########

'''
checking the begining or end of a string
to match text patterns
'''
# filename = './somefile.txt'
# # print(filename.startswith('./'))
# # print(filename.endswith('.txt'))
# import os
# files = os.listdir('../')
# for name in files:
#     if name == 'dsa-1':
#         print('dsa')
#     if name == 'str-2':
#         print('str')
#     if name == 'numdt-3':
#         print('nums')
#     if name == 'itorgen-4':
#         print('itors')
#     if name == 'fileio-5':
#         print('fileio')
# from urllib.request import urlopen
# def read_data(name):
#     if name.startswith(('http:', 'https:', 'ftp:')):
#         return urlopen(name).read()
#     else:
#         with open(name) as f:
#             return f.read()


# ######## 2.3 ###########
'''
You want to match text using the same
wildcard patterns as are commonly used 
when working in Unix shells 
(e.g., *.py, Dat[0-9]*.csv, etc.).
fnmatch module provides two functions—
fnmatch() and fnmatchcase()
'''
# from fnmatch import fnmatch, fnmatchcase
# print(fnmatch('foo.txt', '*.txt'))
# print(fnmatch('foo.txt', '?oo.txt'))
# print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
# MOST USEFUL FOR MATCH CAES QUERYS:
# addresses = [
#         '5412 N CLARK ST',
#         '1060 W ADDISON ST',
#         '1039 W GRANVILLE AVE',
#         '2122 N CLARK ST',
#         '4802 N BROADWAY',
# ]
# print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
# print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])


# ######## 2.4 ###########
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
tests = [text1, text2]
# import re
# # Simple matching: \d+ means match one or more digits
# for item in tests:
#     if re.match(r'\d+/\d+/\d+', item):
#         print('Y')
#     else:
#         print('N')
'''
if you are going to be repeting the pattern
you can compile it for ease of access
'''

# datepat = re.compile(r'\d+/\d+/\d+')
# for item in tests:
#     if datepat.match(item):
#         print('Yes')
#     else:
#         print('No')
        
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# print(datepat.findall(text))
'''
When defining regular expressions, 
it is common to introduce capture groups by en
closing parts of the pattern in parentheses.
Capture groups often simplify subsequent processing 
of the matched text because the contents of each 
group can be extracted individually.
'''
import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))