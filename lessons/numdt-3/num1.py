# Ch2 L 1-4
######################################
################ 3.1 #################
######################################
'''
You want to round a floating-point 
number to a fixed number of decimal 
places.
'''
# print(round(1.23)) #= 1
# print(round(1.23, 1)) #= 1.2
# print(round(1.23, 2)) #= 1.23
# print(round(1.234, 2)) #= 1.23
# print(round(-1.23, 1)) #= -1.2
# a = 167731
# print(round(a, -1)) #= 167730
'''
Dont confuse rounding with formating
numbers for output. If you just want to
display the nuber to the nearest decimal
'''
# x = 1.23456
# print(format(x, '0.2f')) #= 1.23
# print(format(x, '0.3f')) #= 1.235
# print('The value is: {:0.3f}'.format(x)) #= The value is: 1.235
'''
Also resist the urge to round to fix
percieved accuracy problems. Most are
tolerated by the language or minor but
for financial app where it is important:
    use the decimal module as in the
    next chapter
'''
######################################
################ 3.2 #################
######################################
'''
If you need to perform accurate calculations
with decimal numbers, and don't want the 
small errors that naturally occur w/floats
&& are willing to give up a little performance
'''
# from decimal import Decimal
# a = Decimal('4.2')
# b = Decimal('2.1')
# print(a+b) #= 6.3
# print((a+b) == Decimal('6.3')) #True

'''
You can also change different aspects 
by creating a localcontext
'''
# from decimal import localcontext
# a = Decimal('1.3')
# b = Decimal('1.7')
# print(a / b)
# with localcontext() as ctx:
#     ctx.prec = 3
#     print(a/ b)
######################################
################ 3.3 #################
######################################

######################################
################ 3.4 #################
######################################