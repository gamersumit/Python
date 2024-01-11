# SET :
# UNORDERED AND UNIQUE COLLECTION OF ITEMS:
# UNORDERED MEANS NO INDEXING:
# in set we can't store list, tules or dictionaries 
# in set we can only store int, float, string
# example = {1,2,3,4,5,6}
# list1 = [1,2,3,1,1,2,3,4,5]
# set_list1 = set(list1)
# print(set_list1)

# example.add(9)
# print(example)

# example.add(9)
# print(example)


# example.remove(9)   # '9' should be present in the example otherwise it will give an error
# print(example)

# example.discard(9) # it will remove '9' if found and won't give error if not found
# print(example)

# print(set_list1.clear()) # clear

# set_list1 = example.copy() # copy
# print(set_list1)

# s1 = {1, 1.0, 2.3} # here 1 and 1.0 will be treated as same values thus only one value will be considered
# print(s1)

# s1.remove(2.3)
# s1.add(3)
# s1.add(2)
# s1.add(4)

# s2 = {1,5,4,8,7,2,9}

# union_set = s1 | s2 # union
# print(union_set)

# inter_set = s1 & s2 # intersection
# print(inter_set)


