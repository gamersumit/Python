# **kwargs // double star operator / / **kwargs
# keyword arguments
# it wi;; gather arguments as dicitonary


################################################################

# def example(**kwargs):
#     print(type(kwargs), kwargs)

# example(anime = 'onepiece', game = 'valorant')


################################################################

## order of parameters in function declearation:

## normal parameters
## *args
## default parameters
## **kwargs

# def example(num1, num2, *args, anime = 'onepiece', game = 'valorant', **kwargs):
#     print(num1, num2)
#     print(args)
#     print(anime, game)
#     print(kwargs)

# example(1,2, 'x', 'y', 'z', anime = 'naruto', name = 'sumit', age = 22)


################################################################
#EXERCISE 2:

# def fun(names, **kwargs):
#         if kwargs.get('reverse_str') :
#            print([name[::-1].title() for name in names])

#         else:
#               print([name.title() for name in names])

# fun(['sumit', 'prashant', 'lalit', 'onkar'])

# fun(['sumit', 'prashant', 'lalit', 'onkar'], reverse_str = True)




