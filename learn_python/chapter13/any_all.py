# any and all function:
# all -> if all values inside a list are true it will return true else false
# any -> if any values inside a list is true it will return true else false
# print(all([True, True, True, True, True, True, True, True, True, True, True]))
# print(all([True, True, True, False, True, True]))

# print(any([False, False, False, False, False, False, True, False]))
# print(any([False, False, False, False, False, False, False, False]))


################################################################

# number1 = [2,4,6,7,8,10,12]
# number2 = [4,8,16,20,24,32,36]

# print(all([i%2==0 for i in number1]))
# print(all([i%2==0 for i in number2]))

################################################################
## practice :

# def add(*args):
#         total = 0
#         for num in args:
#             total += num
#         return total

# ## print(add(2,3,4,5,5.6,2.3,'sumit')) ## will give an error as 'sumit' is not a int or float type

# def add2(*args):
#       if(all(type(arg) == int or type(arg) == float for arg in args)) :
#         total = 0
#         for num in args: total += num
#         return total
      
#       else : return -1

# print(add2(2,3,4,5,5.6,2.3,'sumit'))

