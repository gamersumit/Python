# tuples are immutable
# tuples are faster than lists

# example = ('one', 'two', 'three')
# days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
# single = (5)
# print(type(single))

# single = (5,)
# print(type(single))

# word = 'fire'
# print(type(word))

# words = 'fire',
# print(type(words))

# words = 'fire', 'water', 'air', 'earth'
# print(type(words))

# # tuple unpacking

# elements = ('1', '2', 43, '4')
# a,b,c,d = elements
# print(a,b,c,d,type(a),type(b),type(c))

# # list inside tuples
# favourites = ('food',['game', 'valorant'], 'color', ['anime', 'one piece'], 'manga')
# print(favourites[1].pop())
# # print(favourites.pop()) # error
# favourites[1].append('mutable list')
# print(favourites)

# favourites[1][1] = 'valorant'
# print(favourites)

######################################################################

#FUNCITON RETURNING MULTIPLE VALUES:

# def fun(num1, num2):
#     return num1 + num2, num1 * num2

# print(type(fun(2,3)), fun(2,3))
# a,b = fun(2,3)
# print(type(a), type(b), a, b)
