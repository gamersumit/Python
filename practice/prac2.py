# string practice task : date 9 - 1 - 23

# SOLUTION 1: 
# s1 = input("ENTER FIRST STRING: ")
# s2 = input("ENTER SECOND STRING: ")

# print(s1+s2)

################################

# SOLUTION 2:

# s1 = input("ENTER ANY STRING: ")
# length = 0
# for i in s1:
#     length += 1
# print(length)


################################

# SOLUTION 3:

# word = input("enter any string: ")
# sub = input("enter any substring: ")

# print(bool(word.count(sub)))



################################

# SOLUTION 4:

# word = input("enter any string: ")
# print(word[::-1])



################################

# SOLUTION 5:

# word = input("enter any string: ")
# vow = 'aeiouAEIOU'

# count = 0
# for ch in word:
#     if vow.count(ch) :
#         count += 1
# print(count)



################################

# SOLUTION 6:

# s1 = input("enter first string: ")
# s2 = input("enter second string: ")
# s3 = (s1.lower()).replace(" ", "")
# s4 = (s2.lower()).replace(" ", "")
# s1 = list(s3)
# s2 = list(s4)
# s1.sort()
# s2.sort()
# print(True if s1 == s2 else False)





################################

# SOLUTION 7:

# word = input("enter any string: ")
# word2 = word[::-1]
# print(True if word2 == word else False)



################################

# SOLUTION 8:

# def compress(word):
#     com = ''
#     i = 0
#     while i < len(word):
#         count = 1
#         while i+1 < len(word) and word[i] == word[i+1] :
#             count += 1
#             i += 1
#         com += word[i] + str(count)
#         i += 1
#     return com

# print(compress(input('enter any string: ')))




################################

# SOLUTION 9:

# word = input('ENTER ANY STRING: ')

# word_list = list(word.split(' '))
# word_list.reverse()
# word = str(word_list)
# word = word[2:len(word)-2]
# word = word.replace("', '", " ")
# print(word)


################################

# SOLUTION 10:

# word = input('ENTER ANY STRING: ')
# sub = input('ENTER SUBTRING TO REPLACE: ')
# sub2 = input('ENTER SUBTRING TO REPLACE WITH: ')
# print(word.replace(sub, sub2))