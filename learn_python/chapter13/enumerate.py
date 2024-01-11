# ENUMERATE FUNCTIONS :
# TO TACK THE POSITION OF ITEM IN ITERABLE IN FOR LOOP
 

# without enumerate functon :

# names = ['sumit', 'prashant', 'lalit', 'onkar']
# pos = 0
# for name in names :
#     print(f"{pos} ------> {name}")
#     pos += 1


# # with enumerate functon :
    
# names = ['sumit', 'prashant', 'lalit', 'onkar']

# for pos, names in enumerate(names):
#     print(f"{pos} ------> {names}")

########################################################################

# Excercise 1:

# def search(word, words):
#     for pos, sub in enumerate(words):
#         if word == sub: return pos
#     return -1

# print(search(input('enter word to search: '), input('enter words seperated by comma: ').split(',')))