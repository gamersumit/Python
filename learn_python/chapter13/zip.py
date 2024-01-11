# # # ZIP FUNCTION :
# # # make tuples
# # user_id = [1,2,3,4,5]
# # user_name = ['sumit', 'lalit', 'prashant', 'onkar', 'karan', 'abhiraj']
# # users  = list(zip(user_id, user_name))  # lsit of tuples of user_id and user_names upto 'karan'
# # print(users)


# # print(dict(users))
# # # # a list containing tuples with length 2 each then it can be converted to dictionary

# l = [(1,11), (2,12), (3,13), (4,14), (5, 15)]

# l1, l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))
# new_list = []

# for pair in zip(l1, l2):
#     new_list.append(max(pair))

# print(new_list)