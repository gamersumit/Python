# Dictionaries :
# similar to map in c++
# unordered collection of key : value pairs :
# unordered means no indexing

# dicti = {'key' : 'value', 'game' : 'valorant', 5 : 2}
# print(dicti)
# print(type(dict))
# print(dicti['key'])
# print(dicti[5])
# print(dicti[0]) # will give error as there is no indexing in dictionary

# 2nd method to create a dictionary :

# user = dict(name = 'sumit', game = 'valorant')
# print(user)
# print(user['name'])

##############################################################################
# keys in dictionary are unique and if a key is repeated then it will only override the existing key and value
# like = {'a' : '1', 'b' : '2', 'c' : '3', 'a' : '4'}
# print(like)  # a's value will be overwritten

##############################################################################
## dictionary[dictionary[list[]]]
# user_info = {
#     'user1' :{
#     'name' : 'sumit',
#     'age' : '21',
#     'games' : ['valorant', 'chess', 'fifa', 'coc'],
#     'anime' : ['one piece', 'naruto', 'demon slayer'],
#     },

#     'user2' :{
#         'name' : 'claw',
#         'age' : '20',
#         'games' : ['minecraft', 'god of war', 'propnight'],
#         'anime' : ['classroom of elite', 'black clover', 'bleach'],
#     },
# }

# print(user_info['user1']['anime'][-1])

##############################################################################

# how to add/pop/update data to dictionary:

# user2 = {}
# user2['name'] = 'CLAW'
# user2['age'] = '21'

# print(user2)
# pop_item = user2.pop('name')
# ## user2.popitem() # will randomly pop any element from the dictionary
# print(pop_item)
# print(user2)

# more = {'height' : 5.8, 'weight' : 75}
# user2.update(more)
# print(user2)

# more = {'name' : 'sumit', 'age' : '20'} 
# user2.update(more)    # age will be updated from 21 to 20
 
# print(user2)



##############################################################################
# # IN keyword in dictionary

# example = {"key" : 'value', 1 : 2, 'body' : 'ears'}

# if "body" in example:
#     print('key is present')
# else :
#     print('key is absent')


# if 'ears' in example.values():
#     print('value is present')
# else :
#     print('value is absent')

# print(example.values())  
# print(type(example.values()))

# print(type(example.keys()))
# print(example.keys())

##############################################################################
## looping in dictionary

# user = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6 }
# for i in user:
#     print(i, end = ': ') # keys
#     print(user[i])      # values

##############################################################################
## ITEMS METHOD:

# alpha = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6 }
# alpha_items = alpha.items()
# print(alpha_items)
# print(type(alpha_items))

# for key, value in alpha_items.items():
#     print(f"key is {key} and value is {value}")

##############################################################################
## fromkeys METHOD:

# d = {'name' : 'unknown', 'age' : 'unknown', 'height' : 'unknown'}

# # to create the same dict as d we can use fromkeys:

# same_as_d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# # dict.fromkeys([keys], value) or dict.fromkeys((keys), value)

# ran_dic = dict.fromkeys(range(1,11), 'unknown')
# print(ran_dic)

##############################################################################
## get/copy/clear METHOD:

# simple = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6}

# ## print(simple['z]) # will throw an error as there is no 'z' named key in simple
# # instead :

# print(simple.get('z')) # it will not throw an error instead it will give an output 'None' as default
# # None evaluated to false in conditons
# print(simple.get('z', 'not found')) # now it will not return none instead it will return not found
# print(simple.get('a'))

# new = simple.copy() # deep copy
# new2 = simple # shallow copy
# new.clear() # clear dictionary

##############################################################################
