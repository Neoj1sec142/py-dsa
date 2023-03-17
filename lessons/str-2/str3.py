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
'''
if you are using re exp to process
txt, but are concerned about the 
handling of Unicode characters

by default the re module is already
programmed with knowedge of certain
Unicode character classes. EX: \d - digit
'''
# import re
# num = re.compile('\d+')
# ASCII digits
# print(num.match('123'))
#Arabic digits
# print(num.match('\u0661\u0662\u0663'))

# arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
# print(arabic)

# Be aware of Case folding
# pat = re.compile('stra\u00dfe', re.IGNORECASE)
# s = 'straße'
# print(pat.match(s.upper()))

# ######## 2.11 ###########
'''
if you want to strip unwanted whitespace
'''
# s = '     hello world  \n'
# print(s.strip())

# Character Stripping
# t = '-----hello====='
# print(t.lstrip('-'))
# print(t.rstrip('='))
# print(t.strip('-='))
'''
if you wanted to remove characters
or space from the inside of a string
you would have to use another tecnique
such as replace
'''
# print(s.replace(' ', ''))
# import re
# print(re.sub('\s+', ' ', s))
'''
you can also combine with iterative processes
'''
# EX
# with open('filename') as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         pass

# ######## 2.12 ###########
# s = 'pýtĥöñ\fis\tawesome\r\n'
'''
The first step is to clean up the whitespace. 
To do this, make a small translation table and use translate():
'''
# remap = {
#     ord('\t') : ' ',
#     ord('\f') : ' ',
#     ord('\r') : None
# }
# a = s.translate(remap)
# print(a) #= 'pýtĥöñ is awesome'

'''
As you can see here, whitespace characters such 
as \t and \f have been remapped to a single space. 
The carriage return \r has been deleted entirely.
You can take this remapping idea a step further and build 
much bigger tables. 
For ex- ample, let's remove all combining characters:
'''
# import unicodedata
# import sys
# cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
# b = unicodedata.normalize('NFD', a)
# print(b.translate(cmb_chrs)) #= 'python is awesome'
'''
As another EX here is a translation table that maps all Unicode
decimal digit characters to their equivalent in ASCII
'''
# digitmap = { c: ord('0') + unicodedata.digit(chr(c)) 
#             for c in range(sys.maxunicode)
#             if unicodedata.category(chr(c)) == 'Nd' }
# print(len(digitmap)) #= 650
# x = '\u0661\u0662\u0663' # arabic digits 123
# print(x.translate(digitmap)) #= 123

'''
Yet another technique for cleaning up text involves 
I/O decoding and encoding func- tions. The idea here 
is to first do some preliminary cleanup of the text, 
and then run it through a combination of encode() or decode() 
operations to strip or alter it. For example:
'''
# b = unicodedata.normalize('NFD', s)
# c = b.encode('ascii', 'ignore').decode('ascii')

# ######## 2.13 ###########
'''
You need to format text with some sort of alignment applied.
'''
text = 'Hello Neo'
# print(text.ljust(20))
# print(text.rjust(20))
# print(text.center(20))
'''
All of these characters accept a optional
fill character %=*&/-><
'''
# print(text.ljust(20, '='))
# print(text.rjust(20, '>'))
# print(text.center(20, '*'))

'''
the format function can also be used
to easily align things
'''
# print(format(text, '>20'))
# print(format(text, '^20'))
# print(format(text, '<20'))
'''
if you want a fill character here
specify before the alignment
'''
# print(format(text, '>>20'))
# print(format(text, '*^20'))
# print(format(text, '=<20'))

'''
These format codes can also be used in
the format() method when formatting
multiple values. For example:
'''
# print('{:>10s} {:>10s}'.format('Hello', 'World'))
# x = 1.2345
# print(format(x, '>10')) 
# print(format(x, '^10.2f')) #= 1.23