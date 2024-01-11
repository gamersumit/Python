# FILTER FUNCTION : APPENDS VALUES BASED ON A FUNCTION WHEN THE FUNCTION RETURN TRUE FOR PASSING SAME VALUE

def is_even(value):
    return value % 2 == 0

numbers = [i for i in range(7)]
even_list = [i for i in numbers if i%2 == 0]
print(even_list)


even_list2 = tuple(filter(is_even, numbers))
print(even_list2)

even_list3 = tuple(filter(lambda x: x%2 == 0, numbers))
print(even_list3)