from functools import wraps

# # Decorators: To enhance the functionality of any function

# def deco_func(fun):
#     def inside_func():
#         print("do the enhncing")
#         fun()
#     return inside_func  

# def func1():
#     print("this is function1")

# def func2():
#     print("this is function2")

# var = deco_func(func1)
# var()
# print(var.__name__)

# func2 = deco_func(func2)
# func2()
# print(func2.__name__)

# @deco_func # short way to implement decorator
# def func3():
#     print("this is function3")

# func3()
# print(func3.__name__)


############################################################################

# problem one that might occur : when we pass arguments

# def deco_func(fun):
#     def inside_func():
#         print("do the enhncing")
#         fun()
#     return inside_func  

# @deco_func
# def func1(a):
#     print(a,' is a argument')

# func1(1) # will give error as this func(1) is inside_func() of our decorator which does'nt take arguments currently

# # ------- #
# # FIX :- SOLUTION ---> USE OF *ARGS AND **KWARGS # #
# # ------- #


# def deco_func(fun):
#     def inside_func(*args, **kwargs):  # USE VARIABLE ARGUMENTS
#         print("do the enhncing")
#         fun(*args, **kwargs)          # pass the same here
#     return inside_func  

# @deco_func
# def func1(a):
#     print(a,' is a argument')

# func1(1) 

############################################################################
# problem 2 that might occur : when returning something

# def deco_func(fun):
#     def inside_func(*args, **kwargs):
#         print("do the enhncing")
#         fun(*args, **kwargs)
#     return inside_func  

# @deco_func
# def add(a, b):
#     print(a,b,' are  arguments')
#     return a + b

# print(add(1,2)) # will print none as add(1,2) is equivalent to inisde_func(1,2) of our decorator which does'nt return anythiing

# # ------- #
# # FIX :- SOLUTION ---> return func from inside function # #
# # ------- #

# def deco_func(fun):
#     def inside_func(*args, **kwargs):  
#         print("do the enhncing")
#         return fun(*args, **kwargs)          # return fun(*args, **kwargs)
#     return inside_func  

# @deco_func
# def add(a, b):
#     print(a,b,' are  arguments')
#     return a + b

# print(add(2,3))


# problem 3 : doc_string ---> if we try to print doc string of our func it will print doc string of our inside_function in decorator


def deco_func(fun):
    def inside_func(*args, **kwargs):
        '''THIS DOC IS FOR INSIDER FUNCTION'''
        print("do the enhncing")
        return fun(*args, **kwargs)
    return inside_func  

@deco_func
def func1(a):
    '''THIS DOC IS FOR ORIGINAL FUNCTION'''
    print(a,' is a argument')
    return a

print(func1.__doc__)  # it will print doc string for inside function istead of func1()
print(func1.__name__) # it will print name inside function istead of func1()

# # ------- #
# # FIX :- SOLUTION ---> use module: -> from functools import wraps # #
# # ------- #

def deco_func(fun):
    @wraps(fun)   # here use this line to tell the differnce function between fun and wraps
    def inside_func(*args, **kwargs):
        '''THIS DOC IS FOR INSIDER FUNCTION'''
        print("do the enhncing")
        return fun(*args, **kwargs)
    return inside_func  

@deco_func
def func1(a):
    '''THIS DOC IS FOR ORIGINAL FUNCTION'''
    print(a,' is a argument')
    return a

print(func1.__doc__)  
print(func1.__name__) 