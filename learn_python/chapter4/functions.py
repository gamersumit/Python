# FUNCTIONS :
# def add(a,b,c) :
#     return a+b+c

# print(add(1,2,3))

########################################################################

# def greater(a,b) :
#     if a > b : return a
#     return b

# a,b = input("ENTER TWO NUMBERS: ").split(',')

# print(f"greater of two is: {greater(int(a),int(b))}")

########################################################################

# def greatest(a,b,c) :
#     if a > b :
#         if a > c :
#             return a
#         else :
#             return c
#     else :
#         if b > c :
#             return
#         else :
#             return c
        
# print(greater(1,2,35))

########################################################################
# EXERCISE :

# def isPlaindrome(str) :
#     i = 0
#     j = len(str)-1

#     while i < j :
#         if(str[i] != str[j]): return False
#         i += 1
#         j -= 1

#     return True

# print(isPlaindrome("AMAN"))        

########################################################################

# def isPlaindrome(str) :
#     dup = str[-1: : -1]
#     return dup == str


# print(isPlaindrome("NAMAN"))

########################################################################

# def fibonacci(n = 8) : # default argument
#     first = 0
#     second = 1
    
#     print(0, end=", ")

#     for i in range(1,n) :
#         print(second, end=", ")
#         temp = second + first
#         first = second
#         second = temp

# fibonacci(8)

########################################################################

# GLOBAL SCOPE: 

# x = 5
# a = 6

# def fun() :
#     x = 7 # local x
#     return x

# def fun2() :
#     global a
#     a = 9 # global a
#     return a

# print(fun())
# print(x)

# print(fun2())
# print(a)

########################################################################