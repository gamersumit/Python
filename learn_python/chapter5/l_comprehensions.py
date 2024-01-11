# LIST COMPREHENSIONS:

# EXAMPLE 1:

# square = []
# for i in range(1, 10) :
#     square.append(i**2)

# print(square)

# # ---------- # 

# square2 = [i**2 for i in range(1, 10)]
# print(square2)

########################################################################

# EXAMPLE 2:
# neg = []
# for i in range(1, 10) :
#     neg.append(-i)
# print(neg)

# # # ---------- # 

# neg1 = [-i for i in range(1, 10)]
# print(neg)

########################################################################

# EXAMPLE 3:
# names = ['sumit', 'mohit', 'prashant', 'lalit']
# n1 = []

# for i in names :
#     n1.append(i[0])

# print(n1)

# # # ---------- #

# names1 = ['sumit', 'mohit', 'prashant', 'lalit']
# n2 = [i[0] for i in names1]
# print(n2)

########################################################################

# EXAMPLE 4:
# alpha = ['abc', 'def', 'ghi', 'jkl', 'mno']
# rev = []

# for i in alpha:
#     rev.append(i[::-1])

# print(rev)

# # # ---------- #
# alpha2 = ['abc', 'def', 'ghi', 'jkl', 'mno']
# rev2 = [i[::-1] for i in alpha2]

# print(rev2)

########################################################################

# EXAMPLE 5:
# numbers = list(range(1,20))

# nums1 = []
# for i in numbers:
#     if i%2 == 0:
#         nums1.append(i)

# print(nums1)

# # # ---------- #

# numbers2 = list(range(1,20))

# num2 = [i for i in numbers2 if i%2 == 0]
# print(num2)

########################################################################

# EXAMPLE 6:
# mixed = [True, False, False, 'bye', 1, 5, 0.2, [1, 2, 3, 4]]
# int_str = []

# for i in mixed:
#     if(type(i) == int or type(i) == float) :
#         int_str.append(str(i))
# print(int_str)

# # # ------------- #
# mixed2 = [True, False, False, 'bye', 1, 5, 0.2, [1, 2,3,4]]
# int_str2 = [str(i) for i in mixed2 if type(i) == int or type(i) == float]
# print(int_str2)

########################################################################

# EXAMPLE 7:

# nums = [1,2,5,7,9,4,2,6,7]
# odd_even = []
# for i in nums :
#     if i % 2 == 0 :
#         odd_even.append(i*2)
#     else :
#         odd_even.append(-i)

# print(odd_even)

# # # -------------- #

# num2 = [1,2,5,7,9,4,2,6,7]
# odd_even2 = [i*2 if i % 2 == 0 else -i for i in num2]
# print(odd_even2)

########################################################################

# EXAMPLE 8:

# examp = [[1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]]
# print(examp)

# # # ------------- #
# examp1 = [[i for i in range(1,7)] for j in range(5)]
# print(examp1)