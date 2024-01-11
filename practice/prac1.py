# DATE : 8 - 1 - 23

import random

# write a program to print the folloeing two patterns implementing the nested loop concept

#  *
#  * *
#  * * *
#  * * * *
#  * * * * *

# SOLUTION 1:

# i = 1
# rows = int(input("ENTER NUMBER OF ROWS: "))
# while i <= rows:
#     for j  in range(i) :
#         print("*", end=" ")

#     print()    
#     i += 1    


# SOLUTION 2:    

# i = 1
# rows = int(input("ENTER NUMBER OF ROWS: "))

# while i <= rows:
#     for j in range(i):
#         print(i, end = " ")

#     i += 1
#     print()    

# SOLUTION 3:

# i = 1
# rows = int(input("ENTER NUMBER OF ROWS: "))
# isBacktrack = False

# while 0 < i <= rows:
#     for j in range(i):
#         print("* ", end=' ')

#     if(i == rows):
#         isBacktrack = True

#     if isBacktrack :
#         i -= 1
#     else :
#         i += 1

#     print()                


# solution 4:

# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# i = 1
# rows = int(input("ENTER NUMBER OF ROWS: "))
# idx = 0

# while i <= rows:
#     for j in range(i):
#         print(alphabet[idx], end=" ")
        
#         if idx == 25 :
#             idx = 0

#         else :
#             idx = idx + 1

#     i += 1
#     print()    



# # SOLUTION 5:

# num_start = int(input("ENTER STARTING NUMBER: "))

# while num_start >= 0 :
#     print(num_start, end=" ")
#     num_start = num_start - 7

# SOLTUION 6:

# num  = input("ENTER A NUMBER : ")
# cube = 0

# for digi in num :
#     cube += int(digi)**len(num)

# if cube == int(num):
#     print(f"{num} is an Armstrong number")
# else :
#     print(f"{num} is not an Armstrong number")



# SOLUTION 7: 
# SOLUTION 8:

# for i in range(100, 500) :
#     if( i % 13 == 0 and i % 3 != 0) :
#         print(i, end= ", ")

# SOLUTION 9:

# winning_num = random.randint(1, 100)
# guess = int(input("Please enter your guess: "))

# while guess != winning_num :
#     if(winning_num == guess) :
#      print(" Correct! ")
#     elif(winning_num < guess) :
#         print("too high")
#     else :
#         print("too low")
#     guess = int(input("Please enter your guess: "))


# SOLUTION 10:

# password = input("Enter your password: ")
# special = '@$&!'
# isSpecial = False
# digit = '0123456789'
# isDigit = False
# lower = 'abcdefghijklmnopqrstuvwxyz'
# isLower = False
# upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# isUpper = False

# for i in password :
#     if(not isUpper and upper.count(i)):
#         isUpper = True
#     if(not isDigit and digit.count(i)):
#         isDigit = True
#     if(not isLower and lower.count(i)):    
#         isLower = True
#     if(not isSpecial and special.count(i)):
#         isSpecial = True

# if len(password) > 8 and isUpper and isLower and isDigit and isSpecial :
#     print("VALID PASSWORD")

# else :
#     print("INVALID PASSWORD")


# SOLUTION 11 :

# str = input("please enter a string: ")
# sub = input("Please enter a substring: ")

# print(str.find(sub))


# SOLUTION 12 :
# str = "hello world"
# print(str[::-1])

# SOLUTION 13 :
# l1 = [1,1,6,3,5,2,1,1,3,4,6,9,3,"mango", 3, 'apple', 'mango']
# l2=[]
# for i in l1:
#     if i not in l2 :
#         l2.append(i)

# print(l2)


# SOLUTION 14:

# def isPrime(x):
#     if(x <=2 ) :
#         return True
    
#     for i in range(2, round(x ** 0.5)) :
#         if(x % i == 0) :
#             return False
        
#     return  True


# l1 = [1,2,13,17]
# l2 = [0, 1,2,5,9,12]
# l3 = [1,5,7]

# didBroke = False
# for i in l1 :
#     if not isPrime(i) :
#         print('False')
#         didBroke = True
#         break

# if not didBroke :
#     print('True')



# SOLUTION 15:
# L1 = [0,1,2,6,12,9,3,15]

# i = 0
# while i < len(L1) :
#     L1[i] = L1[i] ** 2
#     i += 1

# print(L1)    
