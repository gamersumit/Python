#   DICTIONARIES COMPREHENSIONS :

# EXAMPLE 1:

# square = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(square)

# # #------------ #

# square2 = {i:i**2 for i in range(1,6)}
# print(square2)

# # #------------ #

# square3 = {f"square of {i}" : i**2 for i in range(1,6)}
# print(square3)

###################################################################

# EXAMPLE 2:

# word = "mississipie"
# word_count = {}

# for i in word:
#     word_count[i] = word.count(i)

# print(word_count)

# # # #------------ #

# word2 = "mississipie"
# word_count2 = {i : word2.count(i) for i in word2}
# print(word_count2)


###################################################################


# EXAMPLE 3:

# d1 = {5:"odd", 6 : "even", 7 : "odd", 8 : "even", 9 : "odd", 10 : "even", 11 : "odd"}

# d2 = {i : ("even" if i % 2 == 0 else "odd" ) for i in range(5,12)}

# print(d1)
# print(d2)