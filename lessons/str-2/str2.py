# ######## 2.5 ###########
'''
Searching and replacing strings
'''
# text = 'yeah, but no, but yeah, but no, but yeah'
# text2 = text.replace('yeah', 'yep')

'''
for more complex patterns use the sub()
in the re module
'''
# text = 'Today is 11/27/2012, PyCon starts 3/13/2013.'
# import re
# print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
'''
if your reusing a pattern with the sub() function
try compiling it first to save efficiency and performace
'''
# text = 'Today is 11/27/2012, PyCon starts 3/13/2013.'
# import re
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# text2 = datepat.sub(r'\3-\1-\2', text)
# print(text2)

'''
for even more complex patterns its possible
to specify a substitution callback function
'''
# from calendar import month_abbr
# def change_date(m):
#     mon_name = month_abbr[int(m.group(1))]
#     return f'{m.group(2)} {mon_name} {m.group(3)}'
# print(datepat.sub(change_date, text))

# ######## 2.6 ###########
'''
You need to search for and possibly
replace text in a case-insensitive manner.
re.INGNORECASE
'''
# text = 'UPPER PYTHON, lower python, Mixed Python'
# import re
# one = re.findall('python', text, flags=re.IGNORECASE)
# two = re.sub('python', 'snake', text, flags=re.IGNORECASE)
# you may need to create a matchcase function for more 
# elaborate cases to switch words following case matching
# def matchcase(word):
#     def replace(m):
#         text = m.group()
#         if text.isupper():
#             return word.upper()
#         elif text.islower():
#             return word.lower()
#         elif text[0].isupper():
#             return word.capitalize()
#         else:
#             return word
#     return replace

# print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

# ######## 2.7 ###########
'''
You're trying to match a text pattern using regular expressions,
but it is identifying the longest possible matches of a pattern. 
Instead, you would like to change it to find the shortest 
possible match.
'''
# import re
# str_pat = re.compile(r'\"(.*)\"')
# text1 = 'Computer says "no."'
# text2 = 'Computer says "no." Phone says "yes."'
# str_pat.findall(text1)
# print(str_pat.findall(text2))

# ######## 2.8 ###########
'''
You're trying to match a block of text using a regular expression,
but you need the match to span multiple lines.
'''
# import re
# comment = re.compile(r'/\*((?:.|\n)*?)\*/', re.DOTALL)
# text1 = '/* this is a comment */' 
# text2 = '''/* this is a
#         ... multiline comment */ ... '''

# print(comment.findall(text1)) 
# print(comment.findall(text2))