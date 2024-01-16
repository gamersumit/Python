#self--> dicitonaries practice on 16-1 to 16-1
import pdb 

#* 1. Merge Dictionaries:
#* Write a function that takes two dictionaries as input and merges them into a new dictionary. If there are common keys, combine their values. Don't use any built-in functions like update().

# def merge_dict(dict1, dict2):
#     for key in dict2:
#         if key in dict1 : dict1[key] = (dict1[key], dict2[key])
#         else: dict1[key] = dict2[key]
#     return dict1

# d1 = {'name' : 'sumit', 'age' : 21}
# d2 = {'name' : 'aggarwal', 'game' : 'valorant', 'anime' : 'onepiece'}

# print(merge_dict(d1, d2))


#* 2. Nested Dictionary Search:
#* Create a function that searches for a given value in a nested dictionary. The function should return the key path to the value if found, otherwise, return a message indicating that the value was not found.


# def serach_dict(dic, target, path = []):

#     for key, value in dic.items():
#         current_path = path + [key]
    
#         if value == target:
#             return current_path
        
#         if isinstance(value, dict):
#             result = serach_dict(value, target, current_path)
#             if result:
#                 return result

#     return None




# dicti = {
#     'd1' : {
#         'e1' : {
#             'f1' : 21,
#             'f2' : 22,
#         },
#         'e2' : {
#             'f3' : 23,
#             'f4' : 24

#         }
#     } ,
#     'd2' : {
#         'e3' : {
#              'f5' : 25,
#              'f6' : 26
#         },
#     'e4' : {
#             'f7' : 27,
#             'f8' : 28
#         }
#     }
# }

# print(serach_dict(dicti, 27))


#* Frequency Count:
#* Create a function that takes a list of words as input and returns a dictionary with the frequency count of each word. The function should be case-insensitive.

def count_names(names) :
    dic = {}
    for name in names :
        if name.title() not in dic:
            dic[name.title()] = names.count(name)
    
    return dic

names = ['sumit', 'sumit', 'prashant', 'prashant', 'sumit', 'lalit', 'sumit','lalit', 'prashant','prashant']
print(count_names(names))

