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
