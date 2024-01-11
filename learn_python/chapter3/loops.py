# WHILE LOOP:

# i = 1
# while i <= 10:
#     print(f"{i} : hello world")
#     i += 1  

###############################################################
#EXCERCISE 1:

# sum = 0
# num = int(input("ENTER A NATURAL NUMBER: "))
# i = 1

# while i <= num:
#     sum += i
#     i += 1

# print(f"total sum is: {sum}")    

###############################################################
# EXCERCISE 2:

# num = input("ENTER A MULTI DIGIT NUMBER: ")
# i = 0
# total = 0
# while i < len(num):
#     total += int(num[i])
#     i = i + 1

# print(f"sum of its digits: {total}")

###############################################################
# EXCERCISE 3:

# record = ""
# name = input("ENTER YOUR NAME: ")
# i = 0

# while i < len(name) :
#     if name[i] not in record :
#         print(f"# {name[i]} : {name.count(name[i])}")
#         record = record + name[i]
    
#     i = i + 1

# print(f"record: {record}")

###############################################################

# FOR LOOP :

# for i in  range(10) :    # i = 0  intialized and incremented automatically by 1 upto 9
#     print("hello world!")

###############################################################
# num = int(input("Enter a natural number: "))
# sum = 0

# for i in range(num+1) : 
#     sum += i


# print("sum of all natural number upto" + str(num) + " is : " + str(sum))

###############################################################

# num = input("enter a multi digit number: ")
# total = 0

# for i in range(len(num)):
#     total += int(num[i])

# print("total sum of all digits of the number is: " + str(total))

###############################################################

# BREAK & CONTINUE :

# for i in range(10) :
#     if i == 5 :
#         break
#     print("i = " + str(i))

# for i in range(10) :
#     if i == 5 :
#         continue
#     print("i = " + str(i))

################################################################

# winning_num = 28


# result = True

# while result :
#     num = int(input("GUESS A WINNING NUMBER BETWEEN 1 AND 50 : "))
#     if winning_num == num :
#         print (" you won!")
#        result = False

#     elif winning_num < num :
#         print (" guess a little lower")

#     else :
#         print (" guess a little higher")