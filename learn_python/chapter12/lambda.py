# LAMBDA FUNCIONS :
# LAMBDA FUNCTIONS ARE ANONMOUS FUNCTIONS THEY DON'T HAVE NAMES

# add = lambda a,b : a + b
# print(add(2,3))


# multiply = lambda a,b : a*b
# print(multiply(2,3))


################################################################
# LAMBDA EXPRESSION PRCTICE:
################################################################

# EXAMPLE 1:

# def is_even(a):
#     if a%2 == 0: 
#         return True
#     else: 
#         return False

# # #---------- #

# def is_even1(a):
#     if a%2 == 0: 
#         return True
#     return False

# # #---------- #

# def is_even2(a):
#     if a%2 == 0: return True
#     return False

# # #---------- #

# def is_even3(a):
#     return True if a%2 == 0 else False

# # #---------- #

# def is_even4(a):
#     return a%2 == 0

# # #---------- #

# is_even5 = lambda a : a % 2 == 0

# # #---------- #
# print(is_even5(7))

################################################################

# EXAMPLE 2:

# def last_char(s) :
#     return s[-1]

# # #---------- #

# last_char1 = lambda s : s[-1]

# # #---------- #
# print(last_char1('sumit'))

################################################################

# EXAMPLE 3:

# def length(s) : 
#     if len(s) > 5 :
#        return True
#     return False

# # # #---------- #

# length1 = lambda s : len(s) > 5
# length2 = lambda s : True if len(s) > 5 else False 

# print(length1('sumit aggarwal'))

# # # #---------- #

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# # ## mydoubler = lambda a : a * 2 as myfunc(2)  will return  lambda a : a * 2

# print(mydoubler(11))