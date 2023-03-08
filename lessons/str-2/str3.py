# ######## 2.9 ###########
'''
when working with unicode you may need
to have the same underlying repr,
in Unicode certain characters can be
repr w/ more than one valid sequence
of code points.
'''
# s1 = 'Spicy Jalape\u00f1o'
# s2 = 'Spicy Jalapen\u0303o'
# print(f's1 = {s1}') #= Spicy Jalapeño
# print(f's2 = {s2}') #= Spicy Jalapeño
# print(f's1 len = {len(s1)}') #= 14
# print(f's2 len = {len(s2)}') #= 15

'''
this presents an error for programs
that use string comparison since the
strings are the same in theroy but in
realtiy they have diff lengths and code 
points - they should be normalized
'''
# import unicodedata
# t1 = unicodedata.normalize('NFC', s1)
# t2 = unicodedata.normalize('NFC', s2)
# print(t1 == t2)
# print(ascii(t1))
# print(ascii(s2))
'''
suppose you want to remove all 
diacritical marks from some text 
possibly for the purposes of searching
or matching
'''
# print(''.join(c for c in t1 if not unicodedata.combining(c)))

# ######## 2.10 ###########
