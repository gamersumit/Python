# LIST :
# DATA STRUCTURES
# ORDERED COLLECTIONS OF ITEMS

# number = [1,2,3,4,5,6,6,6,7,7,8]
# print(number)
# print(number[2]) # 0 based indexing

# word = ["word1", "word2", "word3"]
# print(word)
# print(word[-1]) 

# mixed = ["word5", 1, 2, 5.6, None, "word6"]
# mixed[2] = "two"
# print(mixed[::-1])

########################################################################
# METHODS :

# fruits = ["apple", "orange", ]
# fruits.append("mango")

# print(fruits)
# print(len(fruits))

# fruits.insert(1, "grapes")
# print(fruits)

# fruits1 = [1,2,3]
# fruits2 = ["a","m","o"]

# fruits3 = fruits1 + fruits2
# print(fruits3)

# fruits1.extend(fruits2)
# print(fruits1)

# fruits2.append(fruits1) # 2-d mixed list
# print(fruits2)

# ########################################################################
# # DELETE DATA FROM LIST :

# print(fruits1)

# fruits1.pop()

# print(fruits1)

# print(fruits1.pop(1))
# print(fruits1) 

# del fruits1[1]
# print(fruits1)

# fruits1.append('a')
# print(fruits1)

# fruits1.remove('a')
# print(fruits1)

# ########################################################################
# # DEEP COPY & SHALLOW COPY  

# numbers = [1,5,8,2,6,4,9,3]
# print(sorted(numbers)) # list won't change but will print a sorted list
# print(numbers)

# numbers.sort()    # list will change/sort permanently
# print(numbers)

# print(fruits1.count(1))

# fruits1.clear() # clear
# print(fruits1)

# fruits1 = numbers # shallow copy
# fruits1[1] = 0
# print(numbers)
# print(fruits1)

# numbers[1] = 2
# print(numbers)
# num_deep = numbers.copy() # deep copy

# num_deep[1] = 0
# print(numbers)
# print(num_deep)

# ########################################################################
# # IS vs ==

# print(fruits1 == numbers)
# print(fruits1 is numbers)
# print(num_deep == numbers)
# print(num_deep is numbers)

# ########################################################################
# JOIN and SPLIT

# strlist = ["Sumit", "Aggarwal","aka","CLAW"]
# name = '#'.join(strlist)
# print(name)

# newlist = name.split('#')
# print(newlist)

# #######################################################################
# LIST(mutable) - STRING(immutable)

##########################################################################
# 2-D list

# matrix = [[1,2,3], [4,5,6], [7,8,9]]

# print(matrix[2][0]) # 7

# for sublist in matrix:
#     for i in sublist :
#         print(i, end= ' ')
#     print()


# print(type(matrix))

##########################################################################

numbers = list(range(1,11))
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

##########################################################################
