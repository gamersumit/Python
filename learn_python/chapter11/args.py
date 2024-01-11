# *args
# takes argument as tuple
# can provide different number of arguments to a single function


# def total(a, b):  #this funciton ca only print sum of two numbers
#     print(a+b)

# def all_total(*args): # this funciton can print sum of multiple numbers or even a single number
#     print(sum(args))

# total(2,3) #valid
# # total(2) #invalid
# # total(2,3,4) #invalid


# all_total() #valid
# all_total(1) #valid
# all_total(2,3) #valid
# all_total(2,3,4) #valid
# all_total(2,3,4,5,6,7,8) #valid

########################################################################

# *args with  normal parameters

# def normal(num1, word, *args):  # syntax should be as it is  
#     print(type(num1), num1)
#     print(type(word), word)
#     print(type(args), args)

# normal(9, 'sentence', 1,2,3,4,5) # first two arguments are for normal parameter thus compulsory


########################################################################
# unpacking of tuples and list arguments

# def multiply(*args):
#     product = 1
#     for i in args:
#         product *= i
#     print(product)


# ls = [2,3,4]
# multiply(ls)
# multiply(*ls) #unpacked ls


########################################################################
# EXCERCISE 1:


# def expo(num, *args):
#     out = None
#     if args :
#         print([i ** num for i in args])
        
#     else:
#         print("you didn't pass the args")
    
    
# ls = [1,2,3,4]
# tu = (1,2,3,4)
# expo(4)
# expo(2, *ls)
# expo(2, *tu)