# advance usage of max and nim functionS:


# to check longest string in a list of strings

# def fun(item):
#     return len(item)

# names = ['sumit', 'prashant', 'lalit', 'onkar', 'karan', 'abhiraj']

# print(max(names, key=fun))

# print(max(names, key= lambda x : len(x)))


########################################################################

# students = [
#             {'name': 'sumit', 'score': 90, 'age': 20},
#             {'name': 'prashant', 'score': 70, 'age': 22},
#             {'name': 'lalit', 'score': 80, 'age':   21}
#             ]

# print(max(students, key= lambda dic : dic.get('score')))
# print(max(students, key= lambda dic : dic.get('score'))['name'])


# students2 = {
#     'sumit': {'score': 90, 'age': 20},
#     'prashant': {'score': 70, 'age': 22},
#     'lalit': {'score': 80, 'age': 21},
# }
# print(students2['sumit']['score'])
# print(max(students2, key=lambda item: students2[item]['score']))
