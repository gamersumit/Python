# variables as function or a function as variable:

# def square(number) :
#     print(number**2)

# x = square
# x(7)

# print(x.__name__)
# print(square.__name__)


################################################################

# FUNCTIONS AS ARGUMENTS:
# def square(number) :
#     return number**2

# l = [1,2,3,4,5]
# print(list(map(square, l)))
# print(list(map(lambda x: x**2, l)))

# def my_map(func, lis):
#     return [func(x) for x in lis]

# print(my_map(square, l))
# print(my_map(lambda x: x**2, l))


################################################################
# # returning a function from a  function (closure)

# def outer_function():
#     def inner_function():
#         print('inside inner function')
#     return inner_function

# var = outer_function()
# print(var.__name__)
# var()            

