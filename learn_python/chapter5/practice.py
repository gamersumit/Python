# self practice on 17-1 from gfg :
################################

''' Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1] '''

# SOLUTION : 

# def swap(newList):
#     if newList:
#         newList[0], newList[-1] = newList[-1], newList[0] # method 1
#         ## start, *middle, end = newList    #method 2: list unpacking
#         ## newList = [end, *middle, start]
#         ### newList = newList[-1:] + nweList[1:-1] + newList[:1] #method3: string slicing
#     return newList
    
# lis = ['a', 1,2,3,4,'b', False, 5]

# print(swap(lis))


#*#######################################################################

'''
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

Examples:  

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]

'''

# SOLUTION:
# def swap(newList, pos1, pos2):
#     newList[pos2-1], newList[pos1-1] = newList[pos1-1], newList[pos2-1]
#     return newList

# lis = [1,2,3,4,5,6,7,8,9,10]
# print(swap(lis,3,5))


#* #########################################################################

'''
Example

Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.

'''

# SOLUTION :
# lis = [i for i in range(1,11)]
# element = 4

# print(element in lis) # method 1
# print(lis.count(element) > 0) # method 2
# print(any(item ==  element for item in lis)) # method 3


#*################################################################

'''
Input: [2, 3, 5, 6, 7]
Output: []
Explanation: Python list is cleared and it becomes empty so we have returned empty list.

'''

# # SOLUTION :

# lis = [i for i in range(1,11)]

# # lis.clear() # method 1
# # lis *= 0 # method 2
# # lis = [] # method 3
# # del lis[:] # method 4
# # while lis: lis.pop() # method 5

# print(lis)


#* #################################################################

'''
Input: list = [4, 5, 6, 7, 8, 9]
Output: [9, 8, 7, 6, 5, 4] 
Explanation: The list we are having in the output is reversed to the list we have in the input.

'''

# SOLUTION :

# lis = [i for i in range(1,11)]

# lis = lis[::-1] # method 1
# lis.reverse() # method 2
# lis = [lis[-(i+1)] for i,j in enumerate(lis)] # method 3
# print(lis)
