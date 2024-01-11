import random

# syntax
# if conditon:
      #code to be executed if contion is true


# age = 18
# if age >= 14:
#     print("user is allowed to play games")
#     print("playing FIFA")

# # PASS STATEMENT : to use empty if statement // never going to use
    
# if age >= 15:
#   #this will give error
#   pass # now it will not give error

# # if-else
# if age >= 14:
#    print("user is allowed to play FIFA")

# else:
#    print("user is not allowed to play FIFA")

################################################################
# EXERCISE 1 : 

# winning_num = random.randint(1, 100) # to generate random in range between 1 and 100
# guess = int(input("ENTER YOUR GUESS BETWEEN 1 AND 100: "))

# if winning_num == guess :
#    print("you win!")

# else :
#     if winning_num > guess :
#         print("too low")

#     else :
#         print("too high")
   
################################################################
# EXCERCISE 2 :

# name  = input("PLEASE ENTER YOUR  NAME: ")
# age =  int(input("PLEASE ENTER YOUR AGE: "))

# if age >= 10 and name[0].upper() == 'A' :
#     print("YOU CAN WATCH THE COCO MOVIE")

# else :
#    print("YOU CANNOT WATCH THE COCO MOVIE")

################################################################

# if-elif-else statements :

# if age <= 0 :
#    print("YOU CANNOT WATCH THE COCO MOVIE")

# elif 0 < age <= 3 :
#    print("FREE TICKET")

# elif 3 < age <= 10  :
#    print("TICKET PRICE : 100 ")

# elif 10 < age <= 60 :
#    print("TICKET PRICE : 150")

# else :
#    print("TICKET PRICE : 200")
   
################################################################
# in KEYWORD & if with in KEYWORD :
   
# if 'S' in "SUMIT" :
#    print("S is present in SUMIT")

# else :
#    print("S is not present in SUMIT")
   
################################################################
   
# name = "SUMIT"

# if name: # it will be true if name string is not empty else it will be false
#    print("name is not empty")

# else: 
#    print("name is not empty")

###############################################################