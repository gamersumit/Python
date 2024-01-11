# SET COMPREHENSIONS: 
# rarely used


#EXAMPLE 1:
# s1 = {1,4,9,16,25,36,49,64,81,100}
# print(s1)

# # # -------- #

# s2 = {i**2 for i in range(1, 11)} 
# print(s2)

# ############################################################
# #Example 2:

# names = ['sumit', 'prashant', 'lalit', 'onkar', 'sandesh']

# n1 = set({})
# for i in names:
#     n1.add(i[0])

# print(n1) 

# # # -------- #

# names2 = ['sumit', 'prashant', 'lalit', 'onkar', 'sandesh']
# n2 = {i[0] for i in names2}

# print(n2)