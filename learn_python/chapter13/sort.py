# sort and sorted funtions:

# fruits = ['grapes', 'mango', 'apple']
# print(fruits)
# print(fruits.sort())
# print(fruits)

# fruits2 = ['grapes', 'mango', 'apple']
# print(fruits2)
# print(sorted(fruits2))
# print(fruits2)

# sort won't work for tuples and sets
# sorted will work for both

################################################################

# guitars = [
#     {'model': 'yamaha f310', 'price': 8400},
#     {'model': 'taylor 814ce', 'price': 45000},
#     {'model': 'faith naptune', 'price': 50000},
#     {'model': 'faith apollo venus', 'price': 35000}
# ]

# guitars.sort(key=lambda x : x.get('price'))
# print(guitars)

# guitars.sort(key=lambda x : x.get('price'), reverse=True)
# print(guitars)

# print(sorted(guitars, key=lambda x : x.get('price')))