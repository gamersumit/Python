import time
import random


#* Problem 1: Timer Decorator
#* Create a decorator that measures the execution time of a function and prints the time taken in seconds.

# def time_count(fun):   # time module imported
#     def wrapper(*args, **kwargs):
#         time_bf = time.time()
#         res = fun(*args, **kwargs)
#         print(f'total time taken by {fun.__name__} is: {time.time() - time_bf} seconds')
#         return res
#     return wrapper

# @time_count
# def print_names(names) :
#     for name in names: print(name)


# names = ['sumit', 'lalit', 'prashant', 'onkar', 'karan', 'abhiraj', 'manseerat']
# print_names


#* Problem 2: Argument Checker Decorator
#* Write a decorator that checks whether the given function has the required number of arguments. If not, raise a ValueError.

# def arg_checker(fun):
#         def wrapper(*args, **kwargs):
#            try: return fun(*args, **kwargs)
#            except TypeError as err: print('type: ' ,err)
#            except ValueError as err: print('value: ', err)
        
#         return wrapper
    

# @arg_checker
# def add(a, b, c = 10):
#     return a + b + c

# # Testing the decorated function
# print(add(5,7,8,5))
# print(add(3,4,'c'))
# print(add(3,4))
# print(add(5,7,4))


#*  Problem 3: Memoization Decorator
#*  Implement a memoization decorator to cache the results of a function and return the cached result if the same arguments are provided again.

# memo = {}
# def memoization(fun):
#     def wrapper(*args):
#         if(memo.get(str(args))) : 
#             print('memo: ', memo.get(str(args)))
#             return memo.get(str(args))
       
#         print('adding: ', str(args))
#         memo[str(args)] = fun(*args) 
#         return memo.get(str(args))
#     return wrapper


# @memoization
# def fibonacci(n):     # 1 1 2 3 5
#     if(n <= 2) : return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(9)) 



#* Problem 4: Retry Decorator
#* Write a decorator that retries executing a function a specified number of times in case of an exception.


# def retry_dec(num):  # random module imported
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             left = num
#             while left != 0:
#                 try : res = func(*args, **kwargs)
#                 except : 
#                     print("failed... retrying...")
#                     left -= 1
#                 else: return res
            
#         return wrapper
#     return decorator
    
# @retry_dec(5)
# def might_fail(var):
#     number  = random.randint(1,var)

#     if number % 2 : print('a' + 4)
#     return number

# print(might_fail(10))

########################################################################

# def fun1(num):
#     def fun2():
#         num -= 1
#         print('num is: ',num)
#     return fun2


# a= fun1(5)
# a()