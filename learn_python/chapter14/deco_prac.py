import time

# EXCERCISE 1:

# def print_st(func):
#     def wrapper(*args):
#         print(f"you are calling {func.__name__} function")
#         print(func.__doc__)
#         return func(*args)
#     return wrapper

# @print_st
# def add(a,b):
#     '''This function takes two numbers as arguments and returns thier sum'''
#     return a + b

# print(add(1,2))


########################################################################

# EXCERCISE 2: 

# def calculate_time(func):
#     def wrapper():
#         t1 = time.time()
#         func()
#         print(time.time()-t1)

#     return wrapper

# @calculate_time
# def fun():
#     for i in range(20):
#         print('counting time...')

# fun()


################################################################

# EXCERCISE 3:

# def only_int(fun):
#     def wrapper(*args):
#         if all([type(arg) == int for arg in args]): return fun(*args)
#         else: print('not all arguments are integers')
#     return wrapper

# @only_int
# def add(*args):
#     print(sum(args))

# add(1,2,3,4)
# add(1,2,3,4,5,'i')

