# GENERATORS:
# GENERATORS ARE ITERATORS:

# ls = [1, 2, 3, 4]    # ITERABLE
# map(lambda x: x, ls) #   ITERATORS


################################################################
## we can only iterate once over iterators but we can iterate as many times as we want on iterables
## iterables are stored in memory (complete list will be stored in memory)
## iterators are stored like one element at a time and then next element will be come in place of previous
## generators are similar to list but they are iterators 
################################################################

# NORAMAL FUNCTION :
# def print_num(num):
#     for i in range(num):
#         print(i)

# print_num(11)


# # GENERATOR FUNCTION:

# def print_num(num):
#     for i in range(num):
#         yield i        # until we demand the next result it will not return anything


# for number in print_num(11):     # demanding number from function()
#     print(number)


################################################################

# def even(num):
#     for i in range(2,num+1,2): yield i 


# x = int(input("Enter a number: "))
# for number in even(x):
#     print(number)


################################################################
# Generator comprehensions :

# square = [i**2 for i in range(11)]   # list comprehensions
# print(square)


# square2 = (i**2 for i in range(11)) # generator comprehensions
# print(square2)
# print(next(square2))
# print(next(square2))

# for i in square2:
#     print(i, end=', ')